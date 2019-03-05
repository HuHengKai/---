import requests
import os
from lxml import etree
import pymysql
#连接数据库,数据库操作
db=pymysql.Connect(host='localhost',port=3306,user='root',
                   passwd='123456',db='tushu', charset='utf8'
                   )
cursor=db.cursor()
def get_html(url):
 headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
 try:
     html=requests.get(url,headers=headers)
     html.encoding=html.apparent_encoding
     if html.status_code==200:
         print("获取源码成功")
 except Exception as e:
     print("获取失败")
 return html.text
def parse_html(html):
    booknames=[]
    bookcode=[]
    html=etree.HTML(html)
    lis=html.xpath("//div[@class='article']/ul[@class='cover-col-4 clearfix']/li")
    jieshaos=html.xpath("//li/div[@class ='detail-frame']/p[@class='detail']/text()")
    print(jieshaos)
    #print(jieshaos)
    titles=html.xpath("//div[@class='detail-frame']/h2/a/text()")
    print(titles)
    # for li in lis:
    #     title=li.xpath(".//div[@class='detail-frame']/h2/a/text()")[0]
    #     print(title)
    #     booknames.append(ti)
    # for jieshao in lis:
    #     jieshao = jieshao.xpath(".//div[@class ='detail-frame']/p[@class='detail']/text()")[0]
    #     print(jieshao)
    # print(jieshao)
    for i in titles:
        titles=i
        cursor.execute("insert into book(`title`) values('{}')".format(titles))
        print("正在保存")
        db.commit()

if __name__=='__main__':
    url='https://book.douban.com/latest?icn=index-latestbook-all'
    html=get_html(url)
    books=parse_html(html)
