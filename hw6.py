#*******************************************************************************************************#
#Name:              陳信志                                                                                                                                                             #
#Class:               企管3C                                                                                                                                                            #
#SID:                 S04410376                                                                                                                                                     #
#Program Name: hw6.py                                                                                                                                                           #
#Function:          爬取PTT表特版文章列表之人氣數量、標題以及該網頁網址                                                                                            #
#Homework:       No.6                                                                                                                                                               #
#Limitations:      Run on Python 3.X                                                                                                                                           #
#Date:               2018/6/19                                                                                                                                                       #
#*******************************************************************************************************#


import requests
from bs4 import BeautifulSoup


def get_data(sc):
    articles = []

    divs = sc.find_all('div', 'r-ent')
    for d in divs:
        if d.find('div', 'nrec').string:
            if d.find('a'):
                href = 'https://www.ptt.cc/{}'.format(d.find('a')['href'])
                title = d.find('a').string
                hot = d.find('span').string
                articles.append({'title': title,
                                 'href': href,
                                 'hot': hot, })

    return articles


def main():
    lor = 110
    url = input('請輸入任一PTT表特版文章列表：')
    res = requests.get(url=url)

    soup = BeautifulSoup(res.text, 'html.parser')

    art_list = get_data(soup)

    print('HW6 Report'.center(lor, '='))
    print('{:^10s}{:^14s}{:>70s}'.format('人氣', '標題', '網頁'))
    print(''.center(lor, '_'))

    for i in range(0, len(art_list)):

        h = art_list[i].get('hot')
        t = art_list[i].get('title')
        u = art_list[i].get('href')

        line = '{:^10s}{:<28s}{:>63s}'.format(h, t, u)
        print(line)

    print('End Of Report'.center(lor, '='), '\n\n')


main()
