import scrapy
from scrapy.loader import ItemLoader
from ..items import SteamItem
from ..pipelines import get_platforms, clean_discount_rate
from ..pipelines import get_original_price, clean_discounted_price, remove_html

class BestSellingSpider(scrapy.Spider):
    name = 'best_selling'
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/?filter=topsellers/']
    
    def parse(self, response):
        games = response.xpath("//div[@id='search_resultsRows']/a")
        for game in games:
            loader = ItemLoader(item=SteamItem(),selector=game, response=response)
            loader.add_xpath("game_url", ".//@href")
            loader.add_xpath("image_url", ".//div[@class='col search_capsule']/img/@src")
            loader.add_xpath("game_name", ".//span[@class='title']/text()")
            loader.add_xpath("release_date", ".//div[@class='col search_released responsive_secondrow']/text()")
            loader.add_xpath("platforms", ".//span[contains(@class,'platform_img') or @class='vr_supported']/@class")
            loader.add_xpath("reviews_summary", ".//span[contains(@class,'search_review_summary')]/@data-tooltip-html")
            loader.add_xpath("discount_rate", ".//div[contains(@class,'search_discount')]/span/text()")
            loader.add_xpath("original_price", ".//div[contains(@class,'search_price_discount_combined')]")
            loader.add_xpath("discounted_price", "(.//div[contains(@class,'search_price discounted')]/text())[2]")
            
            yield loader.load_item()
            
        next_page = response.xpath(".//a[@class='pagebtn' and text()='>']/@href").get()
        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse
            )
            
            
            
