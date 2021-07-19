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
todo изучить и исправить ошибку с отсутствием подгрузки букв в части отзывов.
todo Скорее всего, дело в кодировке при выгрузке из файлов.
todo Вопрос с кавычками в четвертом файле
"""

#from search_page import links
from settings import proxies, headers
from bs4 import BeautifulSoup
import requests
import csv
from pathlib import Path
from os import walk
import codecs


def reviews_parse_from_file(filename, dirname, parsed_last):
    #чтение html из файла
    html = ''
    # f = codecs.open(Path.cwd() / 'files' / filename, 'rb', )
    # for line in f:
    #     html = html + line.decode(encoding='cp1251', errors='ignore')
    # print(f'parsed: {filename}')
    # f.close()

    with codecs.open(Path.cwd() / "TVs" / dirname / filename, mode='rb', encoding='utf8', errors='ignore') as r_file:
        for line in r_file:
            html = html + line
        print(f'parsed: {filename}')

    if int(filename[filename.find('_')+1:filename.find('.')]) <= int(parsed_last):
        return 0

    first_review = False
    if filename[-6] == '1':
        first_review = True
    filename = filename[:filename.find('_')] + '.csv'

    with codecs.open(Path.cwd() / "reviews" / filename, mode='ab+', encoding='cp1251', errors='ignore') as w_file:
        file_writer = csv.writer(w_file, delimiter="#", lineterminator="\r")

        soup = BeautifulSoup(html, 'html.parser')

        # заполняем общий отзыв (первая строка)
        if first_review == True:
            common_result = ''
            common_list = soup.findAll(class_='_16Nb447nub')
            for t in common_list:
                common_result = common_result + t.text
            common_result = common_result.replace('Достоинства', '')
            common_result = common_result.replace('»«', '» «')
            common_review_to_csv = common_result.split('Недостатки')
            if common_review_to_csv != ' # # ':
                file_writer.writerow(common_review_to_csv)

        # заполняем пользовательские отзывы (в пределах одной страницы)
        boxes = soup.findAll(class_='_3IXczk7DdZ')
        for box in boxes:
            box_result = ''
            for t in box:
                box_result = box_result + t.text
            box_result = clear_first(box_result)
            box_result = review_parse(box_result)
            if box_result != [' ', ' ', ' ']:
                file_writer.writerow(box_result)


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
def clear_first(review_result):
    review_result = review_result.replace(review_result[review_result.find('Комментарий:'):], '')
    review_result = review_result.replace("'", '')
    review_result = review_result.replace("'", '')
    review_result = review_result.replace("\n", '')
    review_result = review_result.replace("...", '')
    review_result = review_result.replace(";", '')
    return review_result
def review_parse(review_result):
    exp = ' '
    adv = ' '
    disadv = ' '
    if 'Недостатки: ' in review_result:
        disadv = review_result[review_result.find('Недостатки: ') + len('Недостатки: '):]
    if 'Достоинства: ' in review_result:
        if 'Недостатки: ' in review_result:
            adv = review_result[review_result.find('Достоинства: ') + len('Достоинства: '):review_result.find('Недостатки: ')]
        else:
            adv = review_result[review_result.find('Достоинства: ') + len('Достоинства: '):]
    if 'Опыт использования: ' in review_result:
        if 'Достоинства: ' in review_result:
            exp = review_result[review_result.find('Опыт использования: ') + len('Опыт использования: '):review_result.find('Достоинства: ')]
        elif 'Недостатки: ' in review_result:
            exp = review_result[review_result.find('Опыт использования: ') + len('Опыт использования: '):review_result.find('Недостатки: ')]
        else:
            exp = review_result[review_result.find('Опыт использования: ') + len('Опыт использования: '):]
    return [exp, adv, disadv]

dirname = 'product--televizor-samsung-t27h390six-27-2017=1823115997'
files = walk(Path.cwd() / 'TVs' / dirname)
k = 0
parsed_last = 0

try:
    for data in files:
        for file in data[2]:
            if 'product--' in file and '.html' in file:
                reviews_parse_from_file(file, dirname, parsed_last)
                k += 1
except Exception as ex:
    print(f'Error! {ex}')
finally:
    print(f'Successfully parsed {k} files')

