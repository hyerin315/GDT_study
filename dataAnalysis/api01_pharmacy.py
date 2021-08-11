import pandas
from bs4 import BeautifulSoup
import requests
from openpyxl.workbook import Workbook

#개인발급 API키 - DDOS 공격 방어
apikey = "px4pGv%2FHLf%2FQ8Lfd8JhU3wUuqPZjoZ2KBym1jbYFM5DlbjIsd7UmieCaNWbmKjKeBKByZZn4BQ3344wkrqktAQ%3D%3D"

#약국정보서비스 API
api = "http://apis.data.go.kr/B551182/pharmacyInfoService/getParmacyBasisList?serviceKey=2iBxaKFKnzeyq04AkTe7ZCYjXgKOO6sXWOegK0YOWsgfPk%2FyFKrzqSaEiKFNMSUDX9qffhdPG0ajf0ydWGVzFQ%3D%3D&pageNo=1&numOfRows=10&sidoCd=110000&sgguCd=110019&emdongNm=%EC%8B%A0%EB%82%B4%EB%8F%99&yadmNm=%EC%98%A8%EB%88%84%EB%A6%AC%EA%B1%B4%EA%B0%95&type=json&APPID={key}"

#약국정보 리스트
list_drugs = ["병원명", "종별코드명", "시도명", "주소", "전화번호"]

for list_drug in list_drugs :
    url = api.format(key=apikey)
    req = requests.get(url)
    re = req.text
    soup = BeautifulSoup(re, 'html.parser')

    #병원명
    yadmnm = soup.find_all('yadmnm')
    #종별 코드명
    sggucdnm = soup.find_all('sggucdnm')
    #시도명
    sidocdnm = soup.find_all('sidocdnm')
    #주소
    addr = soup.find_all('addr')
    #전화번호
    telno = soup.find_all('telno')

print("병원명: ", yadmnm)
print("종별코드명: ", sggucdnm)
print("시도명: ", sidocdnm)
print("주소: ", addr)
print("전화번호: ", telno)
