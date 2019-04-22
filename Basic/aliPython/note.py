
'''
前程无忧网站爬取分析
主页：https://www.51job.com

搜索'python'关键字后 链接
https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=

第二页
https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,2.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=

第三页
https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,3.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=

提取网页：https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,4.html


'''

import requests
import re
import os
import random

def UA():
    HEAD=random.choice(['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'])
    headers = {'User-Agent': HEAD}
    return headers

headers=UA()
idx=1
url='https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,'+str(idx)+'.html'
response = requests.get(url,headers = headers)
data=bytes(response.text,response.encoding).decode("gbk","ignore")
print('爬取网页长度：%d' %len(data))
totkey='<div class="rt">.*?共(.*?)条职位.*?</div>'
totpages=re.compile(totkey,re.S).findall(data)[0]
print('共%s条职位' %totpages)

for i in range(0, int(totpages) // 50 + 1):
    url = 'https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,' + str(i + 1) + '.html'
    headers = UA()
    key_item = '<input class="checkbox" type="checkbox" name="delivery_jobid" value="(.*?)"'
    response = requests.get(url, headers=headers)
    try:
        dtldata = bytes(response.text, response.encoding).decode("gbk", "ignore")
    except:
        continue
    item_id = re.compile(key_item, re.S).findall(dtldata)
    # print(item_id)

    '''
    爬取每个招聘页面
    职位名称  '<h1 title="Python开发工程师">'
    公司名称  'target="_blank" title="广州市欣德信息技术有限公司" class="catn">'
    薪资范围  'tHeader_mk.*?<strong>(.*?)</strong>'
    工作地点  '<span class="label">上班地址：</span>(.*?)</p>'
    招聘人数  '招(.*?)人'
    '''
    for j in item_id:
        url = 'https://jobs.51job.com/guangzhou-thq/' + str(j) + '.html?s=01&t=0'
        headers = UA()
        key_zhiwei = r'<h1.*?title="(.*?)">'
        key_gongsi = 'target="_blank" title="(.*?)" class="catn">'
        key_xinzi = 'tHeader_mk.*?<strong>(.*?)</strong>'
        key_didian = '<span class="label">上班地址：</span>(.*?)</p>'
        key_renshu = '<p class="msg ltype" title=".*?招(.*?)人'
        response = requests.get(url, headers=headers)
        try:
            dtldata = bytes(response.text, response.encoding).decode("gbk", "ignore")
        except:
            continue

        filename = '/Users/dai/PycharmProjects/Basic/aliPython/51job/' + str(j) + '.html'
        #os.system('rm -rf ' + filename)
        #f = open(filename, 'w')
        #f.write(dtldata)
        #f.close()
        # print('爬取详情网页长度：%d' % len(dtldata))
        info=[]
        if len(dtldata) > 0 :
            try:
                info.insert(0,re.compile(key_zhiwei, re.S).findall(dtldata))
            except IndexError:
                info.insert(0,' ')
            try:
                info.insert(1,re.compile(key_gongsi, re.S).findall(dtldata)[0].strip())
            except IndexError:
                info.insert(1,' ')
            try:
                info.insert(2,re.compile(key_xinzi, re.S).findall(dtldata)[0].strip())
            except IndexError:
                info.insert(2,' ')
            try:
                info.insert(3,re.compile(key_didian, re.S).findall(dtldata)[0].replace('\t', '').strip())
            except IndexError:
                info.insert(3,' ')
            try:
                info.insert(4,re.compile(key_renshu, re.S).findall(dtldata)[0].strip())
            except IndexError:
                info.insert(4,' ')
            #print(info)
            #print("{0:{1}^50}".format(str(info[0]),chr(12288)))

            print("{0:{5}<50}\t{1:<4}\t{2:<12}\t{3:{5}<40}\t{4:{5}<50}".format(str(info[0]),str(info[4]),str(info[2]),str(info[1]),str(info[3]),chr(12288)))



    print('--------------------------------------------------------------------------------------------------------------------')


'''
职位['Python开发工程师']                                   |人数3   |薪资0.6-1.2万/月  |公司|广州市欣德信息技术有限公司                                     |地点|广州市天河北路                                           |
职位['Python开发工程师']                                   |人数1   |薪资1-1.5万/月    |公司|广州掌昆网络科技有限公司                                      |地点|琶洲保利中悦广场36楼02房                                    |
职位['运维开发/Python开发工程师']                              |人数3   |薪资1-2万/月      |公司|深圳市心云科技有限公司                                       |地点|黄埔大道西76号富力盈隆2908                                  |
职位['云平台 python 高级开发工程师']                            |人数5   |薪资1.5-2万/月    |公司|广东紫晶信息存储技术股份有限公司                                  |地点|广州市番禺区东环街番禺大道北555号天安总部中心23号楼                      |


'''