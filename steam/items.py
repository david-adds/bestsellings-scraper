# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

class SteamItem(scrapy.Item):
    game_url = scrapy.Field()
    image_url = scrapy.Field()
    game_name = scrapy.Field()
    release_date = scrapy.Field()
    platforms = scrapy.Field()
    reviews_summary = scrapy.Field()
    original_price = scrapy.Field()
    discounted_price = scrapy.Field()
    discount_rate = scrapy.Field()
