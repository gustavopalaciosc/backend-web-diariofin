import requests
from bs4 import BeautifulSoup as bs


def articleScrapper(url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        html_content  = requests.get(url, allow_redirects=False, headers=headers).text
        soup = bs(html_content, 'html.parser')
        title = soup.find('h1', class_='titular').text
        subtitle = soup.find('h2', class_='bajada').text
        text_list = [p.get_text(strip=True) for p in soup.find_all('p')][8:]
        article = {'title': title, 'subtitle': subtitle, 'body': text_list}

        return article



  
