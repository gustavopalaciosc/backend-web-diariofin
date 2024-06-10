import requests
from bs4 import BeautifulSoup as bs


def articleScrapper(url):
        html_content  = requests.get(url, allow_redirects=False).text
        soup = bs(html_content, 'html.parser')
        title = soup.find('h1', class_='titular').text
        subtitle = soup.find('h2', class_='bajada').text
        text_list = [p.get_text(strip=True) for p in soup.find_all('p')][8:]
        article = {'title': title, 'subtitle': subtitle, 'body': text_list}

        return article



  
