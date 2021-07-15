"""
Список ссылок на страницы телевизоров с отзывами
По состоянию на 15.07.2021 - 20 первых ссылок из поисковой выдачи
https://market.yandex.ru/catalog--televizory/18040671/list?cpa=0&hid=90639&how=opinions&onstock=1&local-offers-first=0
"""
urls_reviews = [
    'https://market.yandex.ru/product--televizor-xiaomi-mi-tv-4s-43-t2-42-5-2019/665311013/reviews',
    'https://market.yandex.ru/product--televizor-skyline-32yt5900-32-2019/444694892/reviews',
    'https://market.yandex.ru/product--televizor-leff-32h110t-32-2019/476653006/reviews',
    'https://market.yandex.ru/product--televizor-skyline-32yst5970-32-2019/444808804/reviews',
    'https://market.yandex.ru/product--televizor-lg-43uk6200pla-43-2018/177612332/reviews',
    'https://market.yandex.ru/product--televizor-polarline-32pl13tc-32-2019/410706518/reviews',
    'https://market.yandex.ru/product--televizor-xiaomi-mi-tv-4s-55-t2-54-6-2019/475051026/reviews',
    'https://market.yandex.ru/product--televizor-samsung-ue24n4500au-24-2018/648953154/reviews',
    'https://market.yandex.ru/product--televizor-xiaomi-mi-tv-4a-43-t2-43-2020/767547145/reviews',
    'https://market.yandex.ru/product--televizor-samsung-ue32m5500au-31-5-2017/1725489315/reviews',
    'https://market.yandex.ru/product--televizor-lg-49uk6200-49-2018/177612333/reviews',
    'https://market.yandex.ru/product--televizor-samsung-ue43tu7090u-43-2020/677731028/reviews',
    'https://market.yandex.ru/product--televizor-polarline-24pl12tc-24-2019/410706513/reviews',
    'https://market.yandex.ru/product--televizor-lg-32lm6350-32-2019/440851645/reviews',
    'https://market.yandex.ru/product--televizor-skyline-43lst5970-43-2019/484659089/reviews',
    'https://market.yandex.ru/product--televizor-samsung-ue50tu8000u-50-2020/658182002/reviews',
    'https://market.yandex.ru/product--televizor-samsung-ue43tu8000u-43-2020/660577195/reviews',
    'https://market.yandex.ru/product--televizor-samsung-ue50tu7090u-50-2020/677842029/reviews',
    'https://market.yandex.ru/product--televizor-xiaomi-mi-tv-4a-32-t2-31-5-2019/475050001/reviews'
]

def filenames_create(urls):
    filenames = []
    for url in urls:
#       filename = url[url.find('product--'):] + '.csv'
        filename = url[url.find('product--'):]
        filename = filename.replace('/reviews', '')
        filename = filename.replace('https://', '')
        filename = filename.replace('/', '=')
        filenames.append(filename)
    return filenames

filenames = filenames_create(urls_reviews)

for filename in filenames:
    print(filename)
