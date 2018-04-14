import urllib.request


def download_a_file(url):
    urllib.request.urlretrieve(url, 'art.jpg')


download_a_file(r"https://apod.nasa.gov/apod/image/1205/FullMoonriseArn1250.jpg")