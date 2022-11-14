import pandas as pd
from bs4 import BeautifulSoup
import requests
import whois
import lxml


def get_urls(currency: str, years_interval: str) -> list:
    urls = []
    url = 'https://www.indexmundi.com/commodities/'
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Accept-Encoding": "gzip, deflate, sdch, br",
               "Accept-Language": "en-US,en;q=0.8",
               "Cache-Control": "no-cache",
               "dnt": "1",
               "Pragma": "no-cache",
               "Upgrade-Insecure-Requests": "1",
               "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/1\
               07.0.0.0 Safari/537.36'}
    page = requests.get(url, headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    tags = soup.find_all('a', href=True)
    for a in tags:
        if "?commodity" in a['href'] \
                and "currency" not in a['href'] \
                and "index" not in a['href']:
            commodity_url = url + a['href']
            subpage = requests.get(commodity_url, headers)
            subsoup = BeautifulSoup(subpage.content, 'html.parser')
            years_id = "l" + years_interval + "y"
            subtags = subsoup.find_all('a', id=years_id, href=True)
            for suba in subtags:
                curr_soup = subsoup.find_all('select', id="listCurrency")
                for option in curr_soup:
                    for value in option:
                        if value.get_text() == currency:
                            complete_url = url + suba['href'] + "&currency=" + value['value']
                            urls.append(complete_url)
    return urls


urls = get_urls("US Dollar", "20")
print(urls)
print(len(urls))
