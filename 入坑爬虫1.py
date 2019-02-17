import os
import requests
from lxml import etree
import pymysql
#连接数据库,数据库操作
db=pymysql.Connect(host='localhost',port=3306,user='root',
                   passwd='123456',db='tushu', charset='utf8'
                   )
cursor=db.cursor()
url='https://movie.douban.com/top250'
root='D://test6//'
#建立文件夹
try:
    if not os.path.exists(root):
        os.mkdir(root)
        print("文件夹创建成功")
    else:
        print("文件夹已存在")
except:
    print("文件夹不能存在")
#获取网页
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    try:
        html=requests.get(url,headers=headers)
        html.encoding=html.apparent_encoding
        if html.status_code==200:
            print("获取源码成功")
           # print(html.text)
    except Exception as f:
        print("获取失败")
    return html.text
def parser(html):
    html=etree.HTML(html)
    titles=html.xpath("//div[@class='article']/ol[@class='grid_view']/li/div[@class='item']/div[@class='info']/div[@class='hd']/a/span[1]/text()")
    country=html.xpath("//div[@class='article']/ol[@class='grid_view']/li/div[@class='item']/div[@class='info']/div[@class='hd']/a/span[@class='other']/text()")
    jianjie=html.xpath("//li/div[@class='item']/div[@class='info']/div[@class='bd']/p[@class='quote']/span[@class='inq']/text()")
    # print(jianjie)
    # print(len(country))
    # print(titles[0])
    for i in range(0,len(country)):
         # print(country[i])
         # print(titles[i])
         cursor.execute('''insert into books(`title`,`code`,`jianjie`) values ('{}','{}','{}')'''.format(titles[i],pymysql.escape_string(country[i]),jianjie[i]))
         print('正在保存%s'%titles[i])
    print(html)

if __name__=='__main__':
    html=get_html(url)
    parser(html)





