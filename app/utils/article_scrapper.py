import requests
from bs4 import BeautifulSoup as bs
import json
from .get_soup import get_soup
from .title_scrapper import get_title
from .subtitle_scrapper import get_subtitle
from .body_scrapper import get_article_body
from .get_image_url import get_image_url


async def articleScrapper(url):

        try:
                soup = get_soup(url)
                title = get_title(soup)
                subtitle = get_subtitle(soup)
                text_list = get_article_body(soup)
                image_url = get_image_url(soup)
                article = {'status_code': 200, 
                           'title': title,
                           'subtitle': subtitle,
                           'body': text_list,
                           'image_url': image_url}
                return article
        except:
                return {'status_code': 400, 'message': "Error in url article"}



  
if __name__ == "__main__":
        #url = "https://www.df.cl/mercados/banca-fintech/parodi-y-su-ultima-conversacion-con-pinera-estaba-preocupado-por"
        url = "https://www.df.cl/mercados/banca-fintech/la-banca-y-el-retail-financiero-celebran-que-hacienda-incluyera-a-las"
        data = get_soup(url)
        title = get_title(data)
        subtitle = get_subtitle(data)
        body = get_article_body(data)
        image = get_image_url(data)
        print
        print(image)
        


