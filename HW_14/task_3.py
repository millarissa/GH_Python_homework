import csv
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass, fields, astuple
from urllib.parse import urljoin


@dataclass
class Quote:
    quote_text: str
    author: str
    author_born_date: str
    author_born_location: str
    author_bio: str
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

        for i in range(2, 11):
            print(f'Get data from page {i}')
            self.get_next_pages(i, all_quotes)

        return all_quotes

    def get_next_pages(self, i, all_quotes):
        page_url = 'page/' + str(i)
        next_url = urljoin(self.BASE_URL, page_url)
        next_page = requests.get(next_url).content
        page_soup = BeautifulSoup(next_page, 'lxml')
        all_quotes.extend(self.get_single_page_items(page_soup))
        return all_quotes

    def parse_single_item(self, quote_soup: BeautifulSoup):
        author_about = quote_soup.select_one('span a')['href']

        about_page_url = urljoin(self.BASE_URL, author_about)
        about_page = requests.get(about_page_url).content
        about_page_soup = BeautifulSoup(about_page, 'lxml')

        quote_text = quote_soup.select_one('.text').text.replace('“', '').replace('”', '')
        author = quote_soup.select_one('.author').text

        if about_page_soup.select_one('.author-born-date'):
            author_born_date = about_page_soup.select_one('.author-born-date').text
        else:
            author_born_date = 'Birth date is unknown'

        if about_page_soup.select_one('.author-born-location'):
            author_born_location = about_page_soup.select_one('.author-born-location').text.replace('in ', '')
        else:
            author_born_location = 'Birth location is unknown'

        if about_page_soup.select_one('.author-description'):
            author_bio = about_page_soup.select_one('.author-description').text.replace('\n        ', '')
        else:
            author_bio = 'Biography is unknown'

        if quote_soup.select_one('.tags > .keywords')['content']:
            tags = quote_soup.select_one('.tags > .keywords')['content']
        else:
            tags = 'No tags'

        return Quote(
                quote_text=quote_text,
                author=author,
                author_born_date=author_born_date,
                author_born_location=author_born_location,
                author_bio=author_bio,
                tags=tags
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
