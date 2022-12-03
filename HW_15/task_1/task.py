import csv
import random
from dataclasses import dataclass, fields, astuple
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


@dataclass
class Domain:
    field_domain: str
    field_bl: str
    field_domainpop: int
    field_abirth: int
    field_aentries: int
    field_dmoz: str
    field_statuscom: str
    field_statusnet: str
    field_statusorg: str
    field_statustld_registered: int
    field_related_cnobi: str
    field_price: str
    field_endtime: str


class DomainScrapper:
    BASE_URL = 'https://www.expireddomains.net/domain-lists/'
    CATEGORY_URL = '/catched-com-auction-domains/'
    DOMAIN_FIELDS = [field.name for field in fields(Domain)]
    DOMAIN_OUTPUT_CSV_PATH = 'domains.csv'

    def __init__(self):
        self.session = requests.Session()
        self.request_url = urljoin(self.BASE_URL, self.CATEGORY_URL)

    def get_items(self):
        with requests.Session() as session:
            user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
                'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36'
            ]
            user_agent = random.choice(user_agents)
            headers = {'User-Agent': user_agent}

            url = self.request_url
            proxies = {'http': 'http://137.184.197.190:80'}
            page = session.get(url, proxies=proxies, headers=headers)

            page_content = page.content
            first_page_soup = BeautifulSoup(page_content, 'lxml')

            all_domains = self.get_single_page_items(first_page_soup)

            """for i in range(2, 11):
                self.get_next_pages(i, all_domains)"""

            return all_domains

    def get_next_pages(self, i, all_domains):
        page_url = 'page/' + str(i)
        next_url = urljoin(self.BASE_URL, page_url)
        next_page = requests.get(next_url).content
        page_soup = BeautifulSoup(next_page, 'lxml')
        all_domains.extend(self.get_single_page_items(page_soup))
        return all_domains

    def get_single_page_items(self, page_soup: BeautifulSoup):
        domains = page_soup.select('table.base1 tbody tr')
        return [self.parse_single_item(domain_soup) for domain_soup in domains]

    def parse_single_item(self, domain_soup: BeautifulSoup):
        field_domain = domain_soup.select_one('.field_domain a').text
        field_bl = domain_soup.select_one('.field_bl a').text
        field_domainpop = int(domain_soup.select_one('.field_domainpop a').text)
        field_abirth = int(domain_soup.select_one('.field_abirth a').text)
        field_aentries = int(domain_soup.select_one('.field_aentries a').text)

        if domain_soup.select_one('.field_dmoz a'):
            field_dmoz = domain_soup.select_one('.field_dmoz a').text
        else:
            field_dmoz = '-'

        field_statuscom = domain_soup.select_one('.field_statuscom a span').text
        field_statusnet = domain_soup.select_one('.field_statusnet a span').text
        field_statusorg = domain_soup.select_one('.field_statusorg a span').text
        field_statustld_reg = int(domain_soup.select_one('.field_statustld_registered').text)
        field_related_cnobi = domain_soup.select_one('.field_related_cnobi').text
        field_price = domain_soup.select_one('.field_price a').text
        field_endtime = domain_soup.select_one('.field_endtime a').text

        return Domain(
            field_domain=field_domain,
            field_bl=field_bl,
            field_domainpop=field_domainpop,
            field_abirth=field_abirth,
            field_aentries=field_aentries,
            field_dmoz=field_dmoz,
            field_statuscom=field_statuscom,
            field_statusnet=field_statusnet,
            field_statusorg=field_statusorg,
            field_statustld_registered=field_statustld_reg,
            field_related_cnobi=field_related_cnobi,
            field_price=field_price,
            field_endtime=field_endtime
        )

    def write_items_to_csv(self, domains: [Domain]):
        with open(self.DOMAIN_OUTPUT_CSV_PATH, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(self.DOMAIN_FIELDS)
            writer.writerows([astuple(domain) for domain in domains])
        return


if __name__ == '__main__':
    parser = DomainScrapper()
    items_list = parser.get_items()
    parser.write_items_to_csv(items_list)
