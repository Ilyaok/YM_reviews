"""
В данном модуле вводим стартовый url поисковой страницы
Модуль возвращает список ссылок на страницы отзывов, и записывает их в файл
#todo Требуемые доработки:
1. Прохождение по следущим страницам выдачи
2. Улучшение работы прокси (списки или сторонние сервисы).
"""

from bs4 import BeautifulSoup
import requests
from settings import proxies, headers

#здесь вводим стартовый url после поискового запроса на Яндекс.Маркете
start_url = "https://market.yandex.ru/catalog--televizory/18040671/list?cpa=0&hid=90639&how=opinions&onstock=1&local-offers-first=0"

search_page = requests.get(start_url, proxies=proxies, headers=headers)
try:
    search_page.status_code == 200
except:
    print("Ошибка доступа к странице, code=", search_page.status_code)

soup = BeautifulSoup(search_page.text, 'html.parser')

#формируем список ссылок на товары "links'
#пишем список ссылок в файл на случай блокировки

find_all_a = soup.findAll("a", href=True)
links = []

f = open('links_file.txt', 'w')
for t in find_all_a:
    if '/product--' in t['href']:
        link = 'https://market.yandex.ru/' + t['href'] + '/reviews'
        links.append(link)
        f.write(link + '\n')
f.close()

# for link in links:
#     print(link)
#     reviews_page = requests.get(link)
#     soup_reviews = BeautifulSoup(reviews_page.text, 'html.parser')
#     print(link)
