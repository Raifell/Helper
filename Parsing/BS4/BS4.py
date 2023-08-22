from bs4 import BeautifulSoup
import requests

url = 'https://www.parsemachine.com/sandbox/'

page_main = requests.get(url)
soup = BeautifulSoup(page_main.text, features='html.parser')

catalog = soup.find('h2')
link = catalog.find('a')['href']

page_catalog = requests.get('https://www.parsemachine.com' + link)
soup = BeautifulSoup(page_catalog.text, features='html.parser')

count = soup.find_all('div', {'class': 'card product-card'})
for x in count:
    print(x.find('img')['alt'])
    print(x.find('img')['src'])
    print(x.find('a')['href'])
    print()
