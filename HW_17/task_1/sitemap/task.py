from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from sitemap.spiders.sitemap_collect import SitemapCollectSpider

if __name__ == "__main__":
    settings = get_project_settings()
    c = CrawlerProcess(settings)
    c.crawl(SitemapCollectSpider)
    c.start()
