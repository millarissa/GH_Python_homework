from scrapy.crawler import CrawlerProcess

from sitemap.spiders.sitemap_collect import SitemapCollectSpider

if __name__ == "__main__":
    c = CrawlerProcess()
    c.crawl(SitemapCollectSpider)
    c.start()
