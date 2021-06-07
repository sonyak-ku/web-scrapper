import os
import requests
from bs4 import BeautifulSoup
from functions import max_page, scrapping_brand, save_to_file

os.system("clear")
alba_url = "http://www.alba.co.kr"
link = requests.get(alba_url)
soup = BeautifulSoup(link.text, 'html.parser')

brandList = []
goodbox = soup.find(id="MainSuperBrand")
brands = goodbox.find_all('a', {'class': 'goodsBox-info'})

for brand in brands:
    brandDict = {}
    brandDict['brand'] = brand.find('span', {'class': 'company'}).string
    brandDict['link'] = brand['href']
    brandList.append(brandDict)

# 브랜드리스트 완성[{브랜드:이름, 링크:주소},{},...]

for brand in brandList:  # 브랜드리스트를 하나하나 브랜드별로 꺼낸다

    maxPage = max_page(brand)  # 브랜드 맥스페이지추출

    # 브랜드별 job scrapping 시작 , 브랜드의 알바자리들을 보두 리스트에 딕셔너리형태로 넣어 리턴
    jobs = scrapping_brand(brand, maxPage)

    # 스크래핑된 직업들을 csv 형태로 저장!
    save_to_file(brand, jobs)
