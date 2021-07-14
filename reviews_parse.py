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

#from search_page import links
from bs4 import BeautifulSoup
import requests

links = []
f = open('links_file.txt', 'r')
for link in f:
    links.append(link)
f.close()

link1 = 'https://market.yandex.ru/product--televizor-xiaomi-mi-tv-4a-32-t2-31-5-2019/475050001'

def reviews_parse(link):
    filename = link[link.find('product--'):]
    soup =
    f = open(filename, 'w')
    f.write()

reviews_parse(link1)