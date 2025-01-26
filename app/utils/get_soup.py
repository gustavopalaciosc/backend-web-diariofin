import requests
from bs4 import BeautifulSoup as bs


def get_soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')
        return soup
    return None

