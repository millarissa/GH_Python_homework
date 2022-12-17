# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RozetkaItem(scrapy.Item):
    item_id = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    price = scrapy.Field()
    old_price = scrapy.Field()
    brand = scrapy.Field()
    category = scrapy.Field()
