from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('https://market.yandex.ru/catalog--televizory/18040671/list?cpa=0&hid=90639&onstock=1&how=opinions&local-offers-first=0')

driver.find_element_by_link_text('Телевизор Xiaomi Mi TV 4A 32 T2 31.5" (2019), черный').click()
