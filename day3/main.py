import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
from functions import start, informCode, currencyMoney, convertMoney


os.system("clear")

url = "https://www.iban.com/currency-codes"
link = requests.get(url)
soup = BeautifulSoup(link.text, "html.parser")

countryList = []

rows = soup.find_all("tr")[1:]
for row in rows :
  items = row.find_all("td")
  if items[2].text and items[3].text :
    Dict = {}
    Dict['Country'] = items[0].text
    Dict['Currency'] = items[1].text
    Dict['Codes'] = items[2].text
    Dict['number'] = items[3].text
    countryList.append(Dict)



print("Hello! Welcome to Currency Conversion!!!!!!!!!!!!!!!!!!!!!!!!!!!")

for index, country in enumerate(countryList):
  print(f"#{index} {countryList[index]['Country']}")

start(countryList)  



# print(format_currency(5000, "KRW", locale="ko_KR"))