# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SitemapItem(scrapy.Item):
    product_id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
