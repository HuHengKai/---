import requests
from urllib.request import urlretrieve
import urllib.request
import time
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

header1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Cookie': 'SINAGLOBAL=3141879918386.459.1538411299360; UM_distinctid=1672c501435117-0d3f5b3c0907e8-36664c08-e1000-1672c50143820c; _s_tentry=-; Apache=6972725381629.947.1548780514246; ULV=1548780514282:10:4:1:6972725381629.947.1548780514246:1547888337669; SSOLoginState=1549555541; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5PnQ2K.zrqDBLwwTijgZN25JpX5KMhUgL.Fo-cSKBc1h-4Sh.2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMfSo-XSonf1KB4; SCF=ApUTAvtTyy0BISn7UAQezWEO2g8uCmAi8eRq0-OP5rUVv1j_Y-WurOgUQDpmypEwzT1snQ2YoDjXYTeRR1EzI0w.; SUB=_2A25xZX6gDeRhGeNI7lYX-CvFzzWIHXVSE9dorDV8PUNbmtBeLWitkW9NSDvEUlEymMmXbHYB8NgXk08-_gusuo79; SUHB=0A05iTkv1_xSuL; ALF=1581400686; UOR=www.oldding.net,widget.weibo.com,www.google.com; WBStorage=1dbe672167e426cb|undefined',
    'host': 's.weibo.cn',
    'If-Modified-Since': 'Fri, 10 Aug 2018 05:35:48 GMT',
    'If-None-Match': '"ca9511fe6b30d41:f2b"',
    'Referer': 'http://www.rentiyishu55.com/oumeirenti/',
    'Upgrade-Insecure-Requests': 'Upgrade-Insecure-Requests',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
}

while (1):

    url = "https://s.weibo.com/top/summary?cate=realtimehot"
    res = requests.get(url, header1)
    res.encoding = "UTF-8"
    res = res.text
    soup = BeautifulSoup(res, 'lxml')
    list = soup.find(id="pl_top_realtimehot").table.tbody
    # print(list)
    list = list.find_all(name="tr")
    rank = -1
    name_list = []
    num_list = []
    with open('F:/resou.txt', 'a') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')
    for i in list:
        rank += 1
        if (rank == 0):
            continue
        text = i.a.text
        num = i.span.text
        num = int(num)
        name_list.append(text)
        num_list.append(num)
        print(text, num)
        with open('F:/resou.txt', 'a') as f:
            f.write(text + '\n')
            f.write(str(num) + '\n')

    plt.bar(range(len(num_list)), num_list, color='rgb', tick_label=name_list)
    plt.xlabel("热搜话题")
    plt.ylabel("搜索数量")
    Ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    plt.title("实时热搜前五" + Ti)
    plt.show()
    time.sleep(15)