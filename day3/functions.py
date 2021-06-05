import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency


def start(lists):
    print("1.Wanna know currency code 2.Wanna convert currency")
    starts = input("What do you wanna do? 1 or 2\n#: ")
    if(starts == '1'):
        informCode(lists)
    elif(starts == '2'):
        currencyMoney(lists)
    else:
        start()


def informCode(lists):
    print("Please choose select a country by number:")
    retry = 1
    while retry:
        try:
            choose = int(input("#: "))
            if choose < len(lists) and choose >= 0:
                print(f"You chose {lists[choose]['Country']}")
                print(f"The currency code is {lists[choose]['Codes']}")
                retry = 0
            else:
                print("Choose a number from the list!")
        except ValueError:
            print("That wasn't a number.")
        except IndexError:
            print("Choose a number from the list!")


def currencyMoney(lists):
    print("Where are you from? Choose a country by number.\n\n")
    retry1 = 1
    retry2 = 1
    choose1 = 1
    choose2 = 1
    convertList = []
    while retry1:
        try:
            choose1 = int(input("#: "))
            if choose1 < len(lists) and choose1 >= 0:
                print(f"You chose {lists[choose1]['Country']}\n\n")
                convertList.append(lists[choose1]['Codes'])  # put firstcountry
                print("Now choose another country.\n\n")
                retry1 = 0
            else:
                print("Choose a number from the list!")
        except ValueError:
            print("That wasn't a number.")
        except IndexError:
            print("Choose a number from the list!")

    while retry2:
        try:
            choose2 = int(input("#: "))
            if choose2 == choose1:
                print("Don't choose same country!")
            elif choose2 < len(lists) and choose2 >= 0:
                print(f"You chose {lists[choose2]['Country']}\n\n")
                # put secondcountry
                convertList.append(lists[choose2]['Codes'])
                print(
                    f"How many {lists[choose1]['Codes']} do you want to convert to {lists[choose2]['Codes']}.")
                money = int(input("#: "))
                convertList.append(money)  # put money
                retry2 = 0
            else:
                print("Choose a number from the list!")
        except ValueError:
            print("That wasn't a number.")
        except IndexError:
            print("Choose a number from the list!")
    convertMoney(convertList)


def convertMoney(lists):
    currencyUrl = f"https://wise.com/gb/currency-converter/{lists[0]}-to-{lists[1]}-rate?amount={lists[2]}"
    try:
        link = requests.get(currencyUrl)
        soup = BeautifulSoup(link.text, 'html.parser')
        money = float(soup.find('span', {'class': 'text-success'}).string)
        beforeConvert = format_currency(
            lists[2], lists[0].upper(), locale="ko_KR")
        afterConvert = format_currency(
            lists[2]*money, lists[1].upper(), locale="ko_KR")
        print(f"{beforeConvert} is {afterConvert}")
    except AttributeError:
        print("We can't convert money")
