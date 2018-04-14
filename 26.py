import requests
from bs4 import BeautifulSoup
import urllib.request
import random


def download_a_file(url):
    name = random.randrange(1, 100)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)


def trade_spider():
    url = "http://mozillateam.herokuapp.com/"
    fw = open('image_sources.txt', 'w')
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('img', {'alt': 'Image'}):
        src_of_images = link.get('src')
        href = url + src_of_images
        fw.write(href + "\n")
        download_a_file(href)

        # caption_name = link.string
        # get_single_item_data(href)
        # print(caption_name)
        # title = link.string
        # print(title)
    fw.close()

# def get_single_item_data(item_url):
#     source_code = requests.get(item_url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text)
#     for item_name in soup.findAll('p'):
#         print(item_name)


trade_spider()
# get_single_item_data(item_url)
