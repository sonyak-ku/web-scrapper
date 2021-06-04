import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

link = requests.get(url)

html = link.text

soup = BeautifulSoup(html, "html.parser")


row_item = soup.find_all("td")

items = []

for item in row_item:
    items.append(item.text)


max_len = len(items)  # 1072
item_len = int(max_len / 4)  # 268


countryDict = {}

for x in range(item_len):
    countryDict[items[4*x]] = items[4*x+2]

# find no universal currency!!! and delete


findUni = {}

for x in range(item_len):
    findUni[items[4*x]] = items[4*x+1]

for key, value in findUni.items():
    if(value == 'No universal currency'):
        del countryDict[key]


print("Hello! Please choose select a country by number:")

# Show Result!! and link number
countryName = {}

number = 0

for item in countryDict:
    print(f"# {number} {item}")
    countryName[number] = item
    number += 1


retry = 1
while retry:

    try:
        choose = int(input("#: "))
        code = countryName[choose]
        print(f"You chose {code}")
        print(f"The currency code is {countryDict[code]}")
        retry = 0

    except ValueError:
        print("That wasn't a number.")
    except KeyError:
        print("Choose a number from the list!")
