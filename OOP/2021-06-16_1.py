#Web 크롤링
import mport
import requests

mport
requests  #http규격에 맞춰 요청과 응답을 처리하는 모듈 (웹 페이지의 HTML을 가져오는 모듈)
from bs4 import BeautifulSoup  # HTML을 파싱하는 모듈

# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
response = requests.get('https://pythondojang.bitbucket.io/weather/observation/currentweather.html')
response.content
soup = BeautifulSoup(response.content, 'html.parser')
soup.find()
##content_weather > table > tbody > tr:nth-child(1) > td:nth-child(6)
table = soup.find('table', {'class': 'table_develop3'})  # <table class="table_develop3">을 찾음
data = []  # 데이터를 저장할 리스트 생성
for tr in table.find_all('tr'):  # 모든 <tr> 태그를 찾아서 반복(각 지점의 데이터를 가져옴)
    tds = list(tr.find_all('td'))  # 모든 <td> 태그를 찾아서 리스트로 만듦
    # (각 날씨 값을 리스트로 만듦)
    for td in tds:  # <td> 태그 리스트 반복(각 날씨 값을 가져옴)
        if td.find('a'):  # <td> 안에 <a> 태그가 있으면(지점인지 확인)
            point = td.find('a').text  # <a> 태그 안에서 지점을 가져옴
            temperature = tds[5].text  # <td> 태그 리스트의 여섯 번째(인덱스 5)에서 기온을 가져옴
            humidity = tds[9].text  # <td> 태그 리스트의 열 번째(인덱스 9)에서 습도를 가져옴
            data.append([point, temperature, humidity])  # data 리스트에 지점, 기온, 습도를 추가

data  # data 표시. 주피터 노트북에서는 print를 사용하지 않아도 변수의 값이 표시됨
with open('weather.csv', 'w') as file:    # weather.csv 파일을 쓰기 모드로 열기
    file.write('point,temperature,humidity\n')                  # 컬럼 이름 추가
    for i in data:                                              # data를 반복하면서
        file.write('{0},{1},{2}\n'.format(i[0], i[1], i[2]))    # 지점,온도,습도를 줄 단위로 저장
