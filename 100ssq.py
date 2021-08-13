import requests
from bs4 import BeautifulSoup
import datetime
import json
import collections
import csv, codecs
current_date = datetime.datetime.now().strftime('%Y-%m-%d')

headers = {
    'Connection': 'keep-alive' ,
    'Accept': 'application/json, text/javascript, */*; q=0.01' ,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36' ,
    'X-Requested-With': 'XMLHttpRequest' ,
    'Referer': 'http://www.cwl.gov.cn/kjxx/ssq/kjgg/',
    'Accept-Language': 'zh-CN,zh;q=0.9' ,
}

cookies = {
    'Sites':'_21',
    'UniqueID':'ysNpHlKidni3o2KC1628649748324',
    '_ga':'GA1.3.824252998.1628585620',
    '_gid':'GA1.3.1469736669.1628585620',
    '_gat_gtag_UA_113065506_1':'1',
    '21_vq':'32',
}
response = requests.get('http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=100',cookies=cookies,headers=headers)
response.encoding = 'utf-8'
# print(response.text)
soup = BeautifulSoup(response.text,'html.parser')
soup = json.loads(str(soup))
li = soup['result']
red_li = []
blue_li = []
for l in li:
    blue_li.append(l['blue'])
    red_num = l['red'].split(',')
    for num in red_num:
        red_li.append(num)

f = codecs.open('近100期ssq.csv','w',encoding='gbk')
csv_writer = csv.writer(f)
csv_writer.writerow(["号码","次数/总数","百分比",''])
csv_writer.writerow(['------->','红球','<-------',])
for i in range(1,34):
    if i < 10:
        i = '0' + str(i)
    n = red_li.count(str(i))
    csv_writer.writerow([i,str(n)+'/600',str(round(n/600*100,2))+'%'])
csv_writer.writerow(["号码","次数/总数","百分比",''])
csv_writer.writerow(['------->','蓝球','<-------',])

for i in range(1,17):
    if i < 10:
        i = '0' + str(i)
    n = blue_li.count(str(i))
    csv_writer.writerow([i,str(n)+'/100',str(round(n/100*100,2))+'%'])


# f = codecs.open('ssq.csv','w',encoding='gbk')
# csv_writer = csv.writer(f)
# csv_writer.writerow(["号码","次数/总数","百分比",''])
# csv_writer.writerow(['------->','红球','<-------',])

# b = collections.Counter(blue_li)
# for d in b:
#     # print(d,b[d])
#     csv_writer.writerow([d,b[d],''])