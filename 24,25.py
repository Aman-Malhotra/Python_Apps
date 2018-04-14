import requests
from bs4 import BeautifulSoup


def trade_spider():
    url = "http://mozillateam.herokuapp.com/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('p'):
        caption_name = link.string
        print(caption_name)
        # title = link.string
        # print(title)


trade_spider()