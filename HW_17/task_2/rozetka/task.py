from scrapy.crawler import CrawlerProcess

from rozetka.spiders.rozetka_category import RozetkaCategorySpider

if __name__ == "__main__":
    c = CrawlerProcess({
        'FEED_FORMAT': 'csv',
        'FEED_URI': '%(cat_id)s_products.csv',
        'FEED_EXPORT_FIELDS': [
                "item_id",
                "title",
                "price",
                "old_price",
                "brand",
                "category",
                "href"
        ]
    })
    c.crawl(RozetkaCategorySpider)
    c.start()
