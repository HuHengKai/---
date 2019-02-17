from lxml import etree
import requests
from selenium import webdriver
import pymysql
def get_html(url):
 headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
 try:
     html=requests.get(url,headers=headers)
     html.encoding=html.apparent_encoding
     if html.status_code==200:
         print("获取源码成功")
         print(html.text)
 except Exception as e:
     print("获取失败")
 return html.text

def parser(html):
    shouye_ele = etree.HTML(html)
    print(shouye_ele)
    zf_list=shouye_ele.xpath("//div[@class='list-con-box']/ul[@class='pList']/li[1]/div[@class='listCon']/h3[@class='listTit']/a/text()")
    print(zf_list)
    zf_url_list=[]
    for zf_url_lost in zf_list:
        zf_url= 'https://bj.5i5j.com'+zf_url_lost
        print(zf_url)
        zf_url_list.append(zf_url)
        print("成功")
if __name__=='__main__':
    url = 'https://bj.5i5j.com/zufang/huilongguan/'
    html=get_html(url)
    parser(html)



