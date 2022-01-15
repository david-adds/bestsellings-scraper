import scrapy
from ..items import SteamItem
from ..pipelines import get_platforms

class BestSellingSpider(scrapy.Spider):
    name = 'best_selling'
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/?filter=topsellers/']
        
    def parse(self, response):
        steam_item = SteamItem()
        games = response.xpath("//div[@id='search_resultsRows']/a")
        for game in games:
            steam_item['game_url'] = game.xpath(".//@href").get()
            steam_item['image_url'] = game.xpath(".//div[@class='col search_capsule']/img/@src").get()
            steam_item['game_name'] = game.xpath(".//span[@class='title']/text()").get()
            steam_item['release_date'] = game.xpath(".//div[@class='col search_released responsive_secondrow']/text()").get()
            steam_item['platforms'] = get_platforms(game.xpath(".//span[contains(@class,'platform_img') or @class='vr_supported']/@class").getall())
            steam_item['reviews_summary'] = game.xpath(".//span[contains(@class,'search_review_summary')]/@data-tooltip-html").get()
            yield steam_item
            
