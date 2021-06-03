import requests
import os


def clean_url(urls, lists):
    for x in urls.split(','):
        lists.append(x.strip())


def check_url(lists, new):
    for x in lists:
        if(x.endswith('.com') == False):
            print(f"{x} is not a valid URL.")
        else:
            new.append(x)


def make_item_url(lists, real):  # //리스트의 아이템에 https 붙이거나, 소문자변환//#
    for x in lists:
        if(x.startswith('https://') == False):
            real.append('https://' + x.lower())
        else:
            real.append(x.lower())


def up_or_down(real_list):
    for x in real_list:

        try:
            r = requests.get(x)
            if(r.status_code == 200):
                print(f'{x} is up!')
        except:
            print(f'{x} is down!')


answer = 'y'

while answer == 'y':

    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you want to check. (seperated by comma)")

    type_url = input()

    url_list = []
    checked_list = []
    real_url = []

    clean_url(type_url, url_list)

    # print(url_list)

    check_url(url_list, checked_list)

    # print(checked_list)

    make_item_url(checked_list, real_url)

    # print(real_url)

    up_or_down(real_url)

    print("Do you want to start over? y/n")
    answer = input()
    os.system('clear')

print('Ok, bye')

# r = requests.get(a)

# print(r.status_code == requests.codes.ok)
