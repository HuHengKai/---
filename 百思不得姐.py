import requests
import os
import random
import time
from lxml import etree
VIDEOURLS=[]
NAMES=[]
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    try:
        html=requests.get(url,headers=headers)
        html.encoding=html.apparent_encoding
        if html.status_code==200:
            print("获取源代码成功")
    except Exception as e:
        print("获取源代码失败")
    return html.text
def parse_html(html):
    vediourls=[]
    names=[]
    html=etree.HTML(html)
    lis=html.xpath("//div[@class='j-r-list']/ul/li")
    print(len(lis))
    for li in lis:
        title=li.xpath(".//div[@class='j-list-user']/div[@class='u-img']/a/img[@class='u-logo lazy']/@alt")[0]
        viodiourl=li.xpath(".//li[@title='下载视频']/a/@href")[0]
        vediourls.append(viodiourl)
        names.append(title)
    return  vediourls,names
        #print
def downloadvideo(url,name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    if  'baisibudejie' in os.listdir("D:\code"):
        pass
    else:
        os.mkdir(r"D:\code\baisibudejie")
    os.chdir(r"D:\code\baisibudejie")
    video=requests.get(url,headers=headers).content
    with open(name+'.mp4','wb') as f:
        print("正在下载%s" % url)
        f.write(video)


if __name__=='__main__':
    url='http://www.budejie.com/video/3'
    html=get_html(url)
    vediourls=parse_html(html)[0]
    names=parse_html(html)[1]
    for i in range(20):
        downloadvideo(vediourls[i],names[i])
        print("下载成功")
# if  __name__=='__main__':
#     page=int(input("请输入需要下载的页:"))
#     for i in range(page):
#         url = 'http://www.budejie.com/video/'+str(i + 1)
#         html = get_html(url)
#         vediourls = parse_html(html)[0]
#         names = parse_html(html)[1]
#         VIDEOURLS.extend(vediourls)
#         NAMES.extend(names)
#     for i in range(20*page):
#         time.sleep(random.randint(1,4)+random.random())
#         downloadvideo(NAMES[i],VIDEOURLS[i])


