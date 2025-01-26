


def get_subtitle(soup):
    description = soup.find('p', class_='enc-main__description')
    if description:
        return description.get_text(strip=True)
    return None