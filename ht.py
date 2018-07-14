# -*- coding:utf-8 -*-

import requests
from lxml import etree
import time
import aiohttp
#
# url = 'https://movie.douban.com/subject/1292052/'
# data = requests.get(url).text
# s = etree.HTML(data)
# files = s.xpath('//*[@id="content"]/h1/span[1]/text()')
# direc = s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
# time = s.xpath('//*[@id="info"]/span[13]/text()')
# print(files)
# print(direc)
# print(time)

with open('D:/douban.txt', 'w', encoding='utf-8') as f:
    for a in range(10):
        url = 'https://book.douban.com/top250?start={}'.format(a*25)
        data = requests.get(url).text()
        s = etree.HTML(data)
        file = s.xpath('//*[@id="content"]/div/div[1]/div/table')
        time.sleep(3)
        for div in file:
            title = div.xpath("./tr/td[2]/div[1]/a/@title")[0]
            href = div.xpath("./tr/td[2]/div[1]/a/@href")[0]
            f.write("{},{}\n".format(title, href))
            time.sleep(1int(len(title))