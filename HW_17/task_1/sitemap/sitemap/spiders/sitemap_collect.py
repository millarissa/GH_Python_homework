import scrapy
from bs4 import BeautifulSoup

from task_1.sitemap.sitemap.items import SitemapItem


class SitemapCollectSpider(scrapy.Spider):
    name = 'sitemap_collect'
    allowed_domains = ['chrome.google.com']
    BASE_URL = 'https://chrome.google.com/'
    category = 'webstore/sitemap'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

    def start_requests(self):
        self.BASE_URL = f'{self.BASE_URL}{self.category}'
        yield scrapy.Request(
            url=self.BASE_URL,
            callback=self.get_locs
        )

    def get_locs(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        sitemap = soup.find_all('sitemapindex')
        loc_list = sitemap[0].find_all('loc')
        for loc in loc_list:
            loc_link = str(loc).replace('<loc>', '').replace('</loc>', '')
            yield scrapy.Request(
                url=loc_link,
                callback=self.get_extention_link
            )

    def get_extention_link(self, response):
        links_soup = BeautifulSoup(response.text, 'lxml')
        urlset = links_soup.find_all('urlset')
        url_list = urlset[0].find_all('loc')
        for url in url_list:
            extention_link = str(url).replace('<loc>', '').replace('</loc>', '')
            yield scrapy.Request(
                url=extention_link,
                callback=self.parse
            )

    def parse(self, response, **kwargs):
        product_id = response.request.url.split('/')[-1]
        yield SitemapItem(
            product_id=product_id,
            title=response.css('h1.e-f-w::text').get(),
            description=response.css('div.C-b-p-j-Pb::text').get()
        )
