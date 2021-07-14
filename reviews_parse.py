"""
Данный модуль забирает список ссылок из файла или списка и парсит отзывы согласно ТЗ
На выходе csv-файл с разделителем #

Одна карточка товара – один файл. Имя файла формируется из URL
https://market.yandex.ru/product--televizor-xiaomi-mi-tv-4a-32-t2-31-5-2019/475050001

Для имени файла надо взять все, что идет после Yandex.ru – только заменить символ слэша, на, например символ =
Для указанного выше URL имя файла будет
product--televizor-xiaomi-mi-tv-4a-32-t2-31-5-2019=475050001

В самом файле:
Первая строка – два значения из обобщенного отзыва (см первый скриншот)
Все остальные строки из трех полей: поле Опыт использования, поле Достоинства, Поле недостатки.
"""

from bs4 import BeautifulSoup
import requests
#from search_page import links

f = open('links_file.txt', 'r')
# for link in f:
#     print(link)

link = 'https://market.yandex.ru/product--televizor-xiaomi-mi-tv-4a-32-t2-31-5-2019/475050001'

def reviews_parse(link):


