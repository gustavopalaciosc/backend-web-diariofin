import requests
from bs4 import BeautifulSoup as bs
import json


async def getImageUrl(soup):
        try:
                script_tag = soup.find('script', {'type': 'application/ld+json'})

                # Extraer el contenido del script
                json_content = script_tag.string

                # Parsear el contenido JSON
                data = json.loads(json_content)

                # Acceder a la URL de la imagen dentro de "@graph" -> "image" -> "url"
                image_url = data['@graph'][0]['image']['url']

                return image_url
        except:
                return ""



async def articleScrapper(url):

        try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                html_content  = requests.get(url, allow_redirects=False, headers=headers).text
                soup = bs(html_content, 'html.parser')
                title = soup.find('h1', class_='titular').text
                subtitle = soup.find('h2', class_='bajada').text
                text_list = [p.get_text(strip=True) for p in soup.find_all('p')][8:]
                image_url = await getImageUrl(soup)
                article = {'status_code': 200, 
                           'title': title,
                           'subtitle': subtitle,
                           'body': text_list,
                           'image_url': image_url}
                return article
        except:
                return {'status_code': 400, 'message': "Error in url article"}



  
if __name__ == "__main__":
        url = "https://www.df.cl/empresas/construccion/tdlc-ordena-reanudar-proceso-licitatorio-del-duty-free-del-aeropuerto-de"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        html_content  = requests.get(url, allow_redirects=False, headers=headers).text
        soup = bs(html_content, 'html.parser')
        #print(html_content)
        print(articleScrapper(url))


