#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author;Tsukasa

import json
import ssl
import urllib
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import re
import xlwt
#import pandas as pd
#import pymongo


def generate_allurl(user_in_nub, user_in_city):  # 生成url
    url = 'http://' + user_in_city + '.lianjia.com/ershoufang/pg{}/'
    for url_next in range(1, int(user_in_nub)):
        yield url.format(url_next)


def get_allurl(generate_allurl):  # 分析url解析出每一页的详细url
    get_url = requests.get(generate_allurl, 'lxml')
    if get_url.status_code == 200:
        re_set = re.compile('<li.*?class="clear">.*?<a.*?class="img.*?".*?href="(.*?)"')
        re_get = re.findall(re_set, get_url.text)
        return re_get


def open_url(re_get):  # 分析详细url获取所需信息
    res = requests.get(re_get)
    if res.status_code == 200:
        info = {}
        soup = BeautifulSoup(res.text, 'lxml')
        info['标题'] = soup.select('.main')[0].text
        info['总价'] = soup.select('.total')[0].text + '万'
        info['每平方售价'] = soup.select('.unitPriceValue')[0].text
        info['参考总价'] = soup.select('.taxtext')[0].text
        info['建造时间'] = soup.select('.subInfo')[2].text
        info['小区名称'] = soup.select('.info')[0].text
        info['所在区域'] = soup.select('.info a')[0].text + ':' + soup.select('.info a')[1].text
        info['链家编号'] = str(re_get)[33:].rsplit('.html')[0]
        for i in soup.select('.base li'):
            i = str(i)
            if '</span>' in i or len(i) > 0:
                key, value = (i.split('</span>'))
                info[key[24:]] = value.rsplit('</li>')[0]
        for i in soup.select('.transaction li'):
            i = str(i)
            if '</span>' in i and len(i) > 0 and '抵押信息' not in i:
                key, value = (i.split('</span>'))
                info[key[24:]] = value.rsplit('</li>')[0]
        print(info)
        return info


def update_to_MongoDB(one_page):  # update储存到MongoDB
    if db[Mongo_TABLE].update({'链家编号': one_page['链家编号']}, {'$set': one_page}, True): #去重复
        print('储存MongoDB 成功!')
        return True
    return False


def pandas_to_xlsx(info):  # 储存到xlsx
    pd_look = pd.DataFrame(info)
    pd_look.to_excel('链家二手房.xlsx', sheet_name='链家二手房')


def writer_to_text(list):  # 储存到text
    with open('lj.text', 'a', encoding='utf-8')as f:
        f.write(json.dumps(list, ensure_ascii=False) + '\n')
        f.close()


#def main(url):

   # writer_to_text(open_url(url))    #储存到text文件
    # update_to_MongoDB(list)   #储存到Mongodb


if __name__ == '__main__':
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    url='https://gz.lianjia.com/ershoufang/pg1/'
    #context = ssl._create_unverified_context()
    get_url = requests.get(url,headers = headers)
    if get_url.status_code == 200:
        #re_set = re.compile('<li.*?class="clear">.*?<a.*?class="img.*?".*?href="(.*?)"')

        #re_set = re.compile('<li.*?class="clear.*?">.*?<a.*?class=".*?img.*?".*?href="(.*?)"')
        re_set = re.compile('<li.*?class=".*?img.*?".*?href="(.*?)"')
        re_get = re.findall(re_set, get_url.text)
        print(len(re_get))
    #response = urllib.request.urlopen(get_url,context=context)
    f=xlwt.Workbook()
    sheet1=f.add_sheet(u'链家二手房源',cell_overwrite_ok=True)
    rowTitle=[u'标题',u'总价',u'每平方售价',u'建造时间',u'小区名称',u'所在区域',u'链家编号']
    for p in range(0,len(rowTitle)):
        sheet1.write(0,p,rowTitle[p])
    line_cnt=1
    for i in re_get:

        if i.endswith('.html'):
            #print(i)

            get_dtl_url = requests.get(i, headers = headers)
            info = {}
            soup = BeautifulSoup(get_dtl_url.text, 'lxml')
            info['标题'] = soup.select('.main')[0].text
            info['总价'] = soup.select('.total')[0].text + '万'
            info['每平方售价'] = soup.select('.unitPriceValue')[0].text
            #info['参考总价'] = soup.select('.taxtext')[0].text
            info['建造时间'] = soup.select('.subInfo')[2].text
            info['小区名称'] = soup.select('.info')[0].text
            info['所在区域'] = soup.select('.info a')[0].text + ':' + soup.select('.info a')[1].text
            info['链家编号'] = str(i)[34:].rsplit('.html')[0]
            print(info)

            sheet1.write(line_cnt, 0, info['标题'])
            sheet1.write(line_cnt, 1, info['总价'])
            sheet1.write(line_cnt, 2, info['每平方售价'])
            sheet1.write(line_cnt, 3, info['建造时间'])
            sheet1.write(line_cnt, 4, info['小区名称'])
            sheet1.write(line_cnt, 5, info['所在区域'])
            sheet1.write(line_cnt, 6, info['链家编号'])
            line_cnt = line_cnt + 1
    f.save('/Users/dai/PycharmProjects/Basic/lj/lianjiaershoufang.xls')
        #for i in soup.select('.base li'):
        #    i = str(i)
        #    if '</span>' in i or len(i) > 0:
        #        key, value = (i.split('</span>'))
        #       info[key[24:]] = value.rsplit('</li>')[0]
        #for i in soup.select('.transaction li'):
        #    i = str(i)
        #    if '</span>' in i and len(i) > 0 and '抵押信息' not in i:
        #        key, value = (i.split('</span>'))
        #        info[key[24:]] = value.rsplit('</li>')[0]
        #print(info)



     #   return re_get
    #user_in_city = input('输入爬取城市：')
    #user_in_nub = input('输入爬取页数：')

    #Mongo_Url = 'localhost'
    #Mongo_DB = 'Lianjia'
    #Mongo_TABLE = 'Lianjia' + '\n' + str('zs')
    #client = pymongo.MongoClient(Mongo_Url)
    #db = client[Mongo_DB]
    #pool = Pool()
    #for i in generate_allurl('2', 'gz'):
        #main(i)
        #writer_to_text(open_url(get_allurl('https://gz.lianjia.com/ershoufang/pg1/')))  # 储存到text文件
        #pool.map(main, [url for url in get_allurl(i)])