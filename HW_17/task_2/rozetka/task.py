from scrapy.crawler import CrawlerProcess

from rozetka.spiders.rozetka_category import RozetkaCategorySpider

if __name__ == "__main__":
    c = CrawlerProcess()
    c.crawl(RozetkaCategorySpider)
    c.start()
