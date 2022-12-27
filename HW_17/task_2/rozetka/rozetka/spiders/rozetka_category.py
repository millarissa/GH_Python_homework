import scrapy
from scrapy.exceptions import CloseSpider

from task_2.rozetka.rozetka.items import RozetkaItem


class RozetkaCategorySpider(scrapy.Spider):
    name = 'rozetka_category'
    allowed_domains = ['rozetka.com.ua']
    BASE_URL = 'https://rozetka.com.ua/ua'
    cat_name = 'keybords-mice/c80255'
    cat_id = cat_name.split('/')[-1]

    def start_requests(self):
        self.BASE_URL = f'{self.BASE_URL}/{self.cat_name}'
        yield scrapy.Request(
            url=self.BASE_URL,
            callback=self.parse_pages
        )

    def parse_pages(self, response):
        yield self.parse(response)
        pages = response.css('a.pagination__link::text')[-1].get()
        for page in range(2, int(pages)):
            yield scrapy.Request(
                url=f'{self.BASE_URL}/page={page}',
                callback=self.get_links
            )

    def get_links(self, response):
        for item in response.css('li.catalog-grid__cell'):
            item_link = item.css('a.goods-tile__heading::attr(href)').get()
            yield scrapy.Request(
                url=item_link,
                callback=self.get_api_data
            )

    def get_api_data(self, response):
        item_id = response.css('p.product__code::text').get().replace(' ', '')
        api_url = f'https://rozetka.com.ua/api/product-api/v4/goods/get-main?goodsId={item_id}'
        yield scrapy.Request(
            url=api_url,
            callback=self.parse
        )

    def parse(self, response, **kwargs):
        item_info = response.json()['data']
        yield RozetkaItem(
            item_id=item_info['id'],
            title=item_info['title'],
            href=item_info['href'],
            price=item_info['price'],
            old_price=item_info['old_price'],
            brand=item_info['brand'],
            category=item_info['last_category']['title']
        )
