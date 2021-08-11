from bs4 import BeautifulSoup as bs
import requests

html = requests.get("https://search.naver.com/search.naver?query=날씨")
soup = bs(html.text, 'html.parser')

#미세먼지 관련 정보 추출
dustdata_one = soup.find('div', {'class':'detail_box'})
dustdata_all = dustdata_one.findAll('dd') #find_all == findAll : 같은 기능이나 버전 차이로 인해 태그명의 차이가 생김
print(dustdata_all) #find : 전체 구문 파싱, find_all(findAll) : 리스트 형식으로 파싱

#[0] : 미세먼지
fine_dust_code = dustdata_all[0].find('span', {'class':'num'})
fine_dust_con = dustdata_all[0].find('span', {'class':'num'}).text

print(fine_dust_code)
print(fine_dust_con)

