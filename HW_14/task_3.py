import csv
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass, fields, astuple
from urllib.parse import urljoin


@dataclass
class Quote:
    quote_text: str
    author: str
    tags: str


class QuoteScrapper:
    BASE_URL = 'https://quotes.toscrape.com/'
    QUOTE_FIELDS = [field.name for field in fields(Quote)]
    QUOTE_OUTPUT_CSV_PATH = 'quotes.csv'

    def get_quotes(self):
        page = requests.get(self.BASE_URL).content
        first_page_soup = BeautifulSoup(page, 'lxml')
        all_quotes = self.get_single_page_items(first_page_soup)
        print('Get data from first page')
        first_next = first_page_soup.select_one('.pager > .next')
        if first_next:
            i = 2
            next_css = self.get_next_pages(i, all_quotes)

            while next_css:
                print(f'Get data from page {i}')
                next_css = self.get_next_pages(i, all_quotes)
                i += 1

        return all_quotes

    def get_next_pages(self, i, all_quotes):
        page_url = 'page/' + str(i)
        next_url = urljoin(self.BASE_URL, page_url)
        next_page = requests.get(next_url).content
        page_soup = BeautifulSoup(next_page, 'lxml')
        all_quotes.extend(self.get_single_page_items(page_soup))
        next_css = page_soup.select_one('.pager > .next')
        return next_css

    def parse_single_item(self, quote_soup: BeautifulSoup):
        if quote_soup.select_one('.tags > .keywords')['content']:
            return Quote(
                quote_text=quote_soup.select_one('.text').text.replace('“', '').replace('”', ''),
                author=quote_soup.select_one('.author').text,
                tags=quote_soup.select_one('.tags > .keywords')['content']
            )
        return Quote(
            quote_text=quote_soup.select_one('.text').text.replace('“', '').replace('”', ''),
            author=quote_soup.select_one('.author').text,
            tags='No tags'
        )

    def get_single_page_items(self, page_soup: BeautifulSoup):
        quotes = page_soup.select('.quote')
        return [self.parse_single_item(quote_soup) for quote_soup in quotes]

    def write_items_to_csv(self, quotes: [Quote]):
        with open(self.QUOTE_OUTPUT_CSV_PATH, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(self.QUOTE_FIELDS)
            writer.writerows([astuple(quote) for quote in quotes])
        return


if __name__ == '__main__':
    parser = QuoteScrapper()
    quotes_list = parser.get_quotes()
    parser.write_items_to_csv(quotes_list)
