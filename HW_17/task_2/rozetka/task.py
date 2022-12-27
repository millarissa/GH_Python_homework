from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from rozetka.spiders.rozetka_category import RozetkaCategorySpider

if __name__ == "__main__":
    settings = get_project_settings()
    c = CrawlerProcess(settings)
    c.crawl(RozetkaCategorySpider)
    c.start()
