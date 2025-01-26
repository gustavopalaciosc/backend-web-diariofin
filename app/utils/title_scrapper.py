


def get_title(soup):
    title = soup.find('h1', class_='enc-main__title')
    if title:
        return title.get_text(strip=True)
    return None