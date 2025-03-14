import requests
from bs4 import BeautifulSoup


def parsing(item):

    URL = f'https://www.kivano.kg/{item}'

    response = requests.get(url=URL)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        items = []
        item_list = soup.find_all('div', class_='item product_listbox oh')
        for item in item_list[:5]:
            name = item.find('div', class_="listbox_title oh").text.strip()
            description = item.find('div', class_="product_text pull-left").text.replace(name, '', 1).strip()
            price = item.find('div', class_="listbox_price text-center").text.strip().replace('\n', ' ')
            items.append((name, description, price))

        return items
    else:
        return 'Страница не найдена'