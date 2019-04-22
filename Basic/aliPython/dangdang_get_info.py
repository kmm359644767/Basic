'''
课后任务：爬取当当网美容护肤频道的前100页商品以及评论数据。
1.进入http://category.dangdang.com/cid4002644.html 商品列表页，爬100页商品列表页的商品数据。
2.依次进入各商品详情页面，获取商品名、商品评论数、商品价格数据，同时，把各个商品的各评论内容爬下来存储到本地文件，自己设计存储结构，合理即可。
'''

import requests
import re
import random
import math
import json
from bs4 import BeautifulSoup

def UA():
    HEAD=random.choice(['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'])
    headers = {'User-Agent': HEAD}
    return headers

for idx in range(1,2):
    headers=UA()
    page_url='http://category.dangdang.com/pg'+str(idx)+'-cid4002644.html'
    page_result = requests.get(page_url,headers = headers)
    if page_result.status_code == 200:
        id_key = '<li ddt-pit=".*?" class=".*?" id="(.*?)"'
        re_set = re.compile(id_key)
        ids = re.findall(re_set, page_result.text)
        for id in ids:
            item_url='http://product.dangdang.com/'+str(id)+'.html'
            #print(item_url)
            headers = UA()
            dtl_result = requests.get(item_url, headers=headers)
            info = {}
            soup = BeautifulSoup(dtl_result.text, 'lxml')
            #商品名、商品评论数、商品价格
            info['商品名'] = soup.select('title')[0].text
            info['商品评论数'] = soup.select('.pinglun')[0].text.replace('\n','').replace('\t','').rsplit('条评论')[0].strip()
            info['商品价格'] = '¥' + soup.select('#dd-price')[0].text.replace('\n','').replace('\r','').replace('¥','').strip()
            print(info)
            filename = '/Users/dai/Documents/kuang/test/dd_comment_' + str(idx) + '_' + str(id) + '.log'
            with open(filename, 'a', encoding='utf-8')as f:
            #http://product.dangdang.com/index.php?r=comment%2Flist&productId=1066906819&categoryPath=58.31.13.17.00.00&mainProductId=1066906819&mediumId=12&pageIndex=3
            #http://product.dangdang.com/index.php?r=comment%2Flist&productId=1066906819&mainProductId=1066906819&pageIndex=3
                try:
                    for page_idx in range(1, math.ceil(int(info['商品评论数'])/10)+1):
                        comment_url='http://product.dangdang.com/index.php?r=comment%2Flist&productId='+str(id)+'&mainProductId='+str(id)+'&pageIndex='+str(page_idx)
                        print(comment_url)
                        headers = UA()
                        dtl_result = requests.get(comment_url, headers=headers)
                        r1=dtl_result.json()
                        key_comment='<div class="describe_detail">.*?<span>(.*?)</span>.*?</div>'
                        comments=re.compile(key_comment,re.S).findall(r1['data']['list']['html'])
                        for c1 in comments:
                            f.write(c1 + '\n')
                            print('id=['+id+'],内容['+c1+']')
                except:
                    pass
                finally:
                    f.close()





