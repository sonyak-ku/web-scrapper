import csv
import requests
from bs4 import BeautifulSoup


def max_page(brand):

    brand_url = f"{brand['link']}job/brand"
    brand_link = requests.get(brand_url)
    soup = BeautifulSoup(brand_link.text, 'html.parser')
    loc = soup.find(id='NormalInfo')
    try:
        number = int(loc.find('p', {'class': 'jobCount'}).find('strong').text)
        return(number//50 + 1)
    except AttributeError:  # 알바숫자가 0 인경우
        return(0)
    except ValueError:  # 알바숫자가 1,401 처럼 사이에 쉼표가 적혀잇는경우
        number = loc.find('p', {'class': 'jobCount'}).find('strong').text
        rep_number = int(number.replace(",", ""))
        return(rep_number//50 + 1)


def scrapping_brand(brand, maxNum):

    brandJobs = []
    for page in range(maxNum):
        brand_page = (f"{brand['link']}job/brand?page={page + 1}&pagesize=50")
        brand_page_link = requests.get(brand_page)

        soup = BeautifulSoup(brand_page_link.text, 'html.parser')
        rows = soup.find('tbody').find_all('tr')
        for row in rows:
            if row.find('td', {'class': 'title'}):
                pageDict = {}
                pageDict['area'] = row.find(
                    'td', {'class': 'local'}).text.replace('\xa0', '')
                pageDict['company'] = row.find(
                    'span', {'class': 'company'}).string
                try:
                    pageDict['time'] = row.find(
                        'span', {'class': 'time'}).string
                except AttributeError:  # 시간 협의 인 경우
                    pageDict['time'] = row.find(
                        'span', {'class': 'consult'}).string
                pageDict['payType'] = row.find(
                    'span', {'class': 'payIcon'}).string
                pageDict['pay'] = row.find('span', {'class': 'number'}).string
                pageDict['date'] = row.find('td', {'class': 'regDate'}).text
                brandJobs.append(pageDict)

    return brandJobs


def save_to_file(brand, jobs):
    try:
        file = open(f"{brand['brand']}.csv", mode='w')
        writer = csv.writer(file)
        writer.writerow(['place', 'title', 'time', 'paytype', 'pay', 'date'])
        for job in jobs:
            writer.writerow(list(job.values()))
    except FileNotFoundError:  # 이자녹스/비욘드/네이쳐컬렉션  이름에 / 들어가있어 csv생성불가경우
        rename = brand['brand'].replace('/', '_')
        file = open(f"{rename}.csv", mode='w')
        writer = csv.writer(file)
        writer.writerow(['place', 'title', 'time', 'paytype', 'pay', 'date'])
        for job in jobs:
            writer.writerow(list(job.values()))
