


def get_image_url(soup):
    img_tag = soup.find('div', class_='art-img').find('img')
    src = img_tag['src']
    return f'https://www.df.cl{src}'