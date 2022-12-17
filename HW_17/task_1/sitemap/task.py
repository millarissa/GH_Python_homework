from scrapy.crawler import CrawlerProcess

from sitemap.spiders.sitemap_collect import SitemapCollectSpider

if __name__ == "__main__":
    c = CrawlerProcess({
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'sitemap.csv',
        'FEED_EXPORT_FIELDS': [
                "product_id",
                "title",
                "description"
        ]
    })
    c.crawl(SitemapCollectSpider)
    c.start()
