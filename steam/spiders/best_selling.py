import scrapy


class BestSellingSpider(scrapy.Spider):
    name = 'best_selling'
    allowed_domains = ['store.steampowered.com/search/?filter=topsellers']
    start_urls = ['http://store.steampowered.com/search/?filter=topsellers/']

    def parse(self, response):
        pass
