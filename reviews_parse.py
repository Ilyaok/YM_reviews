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
from settings import proxies, headers
from bs4 import BeautifulSoup
import requests
import csv
from pathlib import Path
from os import walk


def reviews_parse_from_file(filename):
    #чтение html из файла
    html = ''
    f = open(Path.cwd() / 'files' / filename, 'rb')
    for line in f:
        html = html + line.decode('utf8')
    f.close()

    soup = BeautifulSoup(html, 'html.parser')

    #заполняем общий отзыв (первая строка)
    common_result = ''
    common_list = soup.findAll(class_='_16Nb447nub')

    for t in common_list:
        common_result = common_result + t.text

    common_result = common_result.replace('Достоинства', '')
    common_result = common_result.replace('»«', '» «')
    common_review_to_csv = common_result.split('Недостатки')

    # review_list = soup.findAll(class_='_272cj8YvHe')
    # print(review_list)

    filename = filename.replace('.html', '.csv')
    with open(Path.cwd() / 'reviews' / filename, mode='w') as w_file:
        file_writer = csv.writer(w_file, delimiter="#", lineterminator="\r")
        file_writer.writerow(common_review_to_csv)


def reviews_parse_from_html(url):
    """Выгрузка данных из html На данный момент реализована только выгрузка общего отзыва"""
#   выгрузка html с сайта непосредственно
    html = requests.get(url, proxies=proxies, headers=headers)
    if 'captcha' in html.text:
        print('Captcha detected, please change proxy in settings.py')
    soup = BeautifulSoup(html, 'html.parser')
    common_result = ''

    common_list = soup.findAll(class_='_16Nb447nub')
    for t in common_list:
        common_result = common_result + t.text

    common_result = common_result.replace('Достоинства', '')
    common_result = common_result.replace('»«', '» «')
    common_review_to_csv = common_result.split('Недостатки')

    #формируем имя файла
    filename = url[url.find('product--'):] + '.csv'
    filename = filename.replace('/reviews', '')
    filename = filename.replace('/', '=')

    with open(Path.cwd() / 'reviews' / filename, mode='w') as w_file:
        file_writer = csv.writer(w_file, delimiter="#", lineterminator="\r")
        file_writer.writerow(common_review_to_csv)


files = walk(Path.cwd() / 'files')
k = 0
try:
    for data in files:
        for file in data[2]:
            if 'product--' in file and '.html' in file:
                reviews_parse_from_file(file)
                k += 1
except:
    print('Something went wrong')
finally:
    print(f'Successfully parsed {k} files')

