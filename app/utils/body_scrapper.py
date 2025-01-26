



def get_article_body(soup):
    div = soup.find('div', class_='CUERPO', id='articleLock')
    if div:
        paragraphs = div.find_all('p')
        text_paragraphs = []

        for p in paragraphs:
            text = p.get_text(strip=True)
            if text:  
                text_paragraphs.append(text)
        return text_paragraphs
    return None