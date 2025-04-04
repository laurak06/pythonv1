import requests
from bs4 import BeautifulSoup

URL = 'https://www.kivano.kg/mobilnye-telefony'

response = requests.get(url=URL)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'xml')
    telephones = []
    telephone_list = soup.find_all('div', class_='item product_listbox oh')
    for telephone in telephone_list:
        name = telephone.find('div', class_="listbox_title oh").text.strip()
        description = telephone.find('div', class_="product_text pull-left").text.replace(name, '', 1).strip()
        price = telephone.find('div', class_="listbox_price text-center").text.strip().replace('\n', ' ')
        telephones.append((name, description, price))
else:
    print('Страница не найдена')
