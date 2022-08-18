from selenium import webdriver
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'C:\\Users\\MASTER\\Desktop\\driver\\chromedriver.exe')
driver.get("https://www.kobis.or.kr/kobis/business/stat/boxs/findWeeklyBoxOfficeList.do")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

##content_weather > table > tbody > tr:nth-child(1) > td:nth-child(6)
tbody = soup.find('tbody', id='tbody_0')
span = soup.find('span', class_='ellip per90')
print(span)
