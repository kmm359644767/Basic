#云栖社区 主题抓取
#https://yq.aliyun.com

import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
url='https://yq.aliyun.com/'
key1='<a.*?href="/articles/(.*?)".*?class="alllink"'
get_url = requests.get(url,headers = headers)
if get_url.status_code == 200:
    re_set = re.compile(key1)
    re_get = re.findall(re_set,get_url.text)
    print('获取%d个url' % len(re_get))
    for i in re_get:
        print('https://yq.aliyun.com/articles/%s' % i)
        dtl_url='https://yq.aliyun.com/articles/' + i
        #print(dtl_url)
        get_article_url = requests.get(dtl_url, headers=headers)
        if get_article_url.status_code == 200:
            #print('获取明细中。。。')
            info = {}
            soup = BeautifulSoup(get_article_url.text, 'lxml')
            info['标题'] = soup.select('title')[0].text
            #b-author
            info['作者'] = soup.select('.b-author')[0].text
            info['摘要'] = soup.select('.blog-summary')[0].text
            print(info)

