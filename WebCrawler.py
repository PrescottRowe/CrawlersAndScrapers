import requests                         #request information from a webpage
from bs4 import BeautifulSoup           #tools to sort through HTML to grab specified data

def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.somesite.com/directory?page=' + str(page)
        html_code = requests.get(url)
        plain_text = html_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.find_all('div', {'class': 'product-grid-item__brand'}):
            #href= "https://www.somesite.com" + link.get('href')
            title = link.string
            # print(href)
            print(title)
        page+=1


spider(1)
