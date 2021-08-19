import pandas as pd
from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import re
import random
import requests

driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')                   #크롬드라이브 연결

def move_page(page):           #카페 검색창 링크 가져오기
    url='https://section.cafe.naver.com/ca-fe/home/search/articles?q="제로 웨이스트"&p='+str(page)+'&od=1&pr=7&ps=2021.04.01&pe=2021.04.21'
    return url

def no_space(text):            #가져온 텍스트 띄어쓰기 없애는 함수
    text1=re.sub('\n','',text)
    return text1

def get_data(driver):                   #카페에서 제목, 시간(날짜), 본문 가져오는 함수
    driver.switch_to.frame("cafe_main")

    html = driver.page_source
    soup = bs(html, 'html.parser')

    Date=soup.find('span',{'class':'date'}).text

    try:
        Like=soup.find('em',{'class':'u_cnt _count'}).text
    except:
        Like='0'
    Like=int(Like)

    try:
        Content = soup.find('div', {'class': 'article_viewer'}).text.strip()
    except:
        Content=''
    Content=no_space(Content)

    try:
        Hashtag = soup.find('a', {'class': 'tag_link'}).text.strip()
    except:
        Hashtag = ''

    data=[Date,Like,Content,Hashtag]
    return data

result=[]
hrefs_list=[]

for page in range(48):              #페이지수 입력하고 그만큼 페이지 넘기기
    url=move_page(page)
    driver.get(url)
    time.sleep(1)
    article_list = driver.find_elements_by_css_selector('a.item_subject')

    html = driver.page_source
    soup = bs(html, 'html.parser')
    rink=soup.find_all('div',{'class':'detail_area'})
    hrefs=[div.find('a')['href'] for div in rink]
    for i in range(10):
        hrefs_list.append(hrefs[i])

    for article in article_list:            #페이지에 있는 글 클릭하여 들어갔다가 다시 나오고 탭 닫기
        article.click()
        time.sleep(2)

        change_tab = driver.window_handles[-1]
        driver.switch_to.window(change_tab)

        #result.append(hrefs[n])
        #n += 1

        try:
            data=get_data(driver)               #클릭해서 들어간 글에서 원하는 거 긁어오기
            result.append(data)
        except:
            pass

        driver.close()

        change_tab = driver.window_handles[-1]
        driver.switch_to.window(change_tab)


#print(len(result))
print(result)


df=pd.DataFrame(result,columns=['Date','Like','Content','Hashtag'])
#df = df.join(pd.Series(hrefs).rename('URL'), how='right')
df.insert(0,"URL",pd.Series(hrefs_list),True)
print(df)

#df.to_excel('친환경 세제.xlsx')
df.to_csv('제로웨이스트0401_0421.csv',index=False, encoding="utf-8-sig")

