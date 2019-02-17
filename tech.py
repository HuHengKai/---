import requests
import os
import pandas as pd
from lxml import etree
def get_html(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    try:
        html=requests.get(url,headers=headers)
        html.encoding=html.apparent_encoding
        if html.status_code==200:
            print("成功获取源码")
            #print(html.text)
    except Exception as e:
        print('抓取代码失败：%s'%e)
    return html.text
def parse_html(html):
    html=etree.HTML(html)
    tables=html.xpath("//div[@class='indent']//table")
    books=[]
    imgurls=[]
    for t in tables:
        title=t.xpath(".//td[@valign='top']//a/@title")[0]
        author=t.xpath(".//td[@valign='top']//p[1]/text()")[0].split('/')[0]
        price=t.xpath(".//td[@valign='top']//p[1]/text()")[0].split('/')[-1]
        press_time=t.xpath(".//td[@valign='top']//p[1]/text()")[0].split('/')[-2]
        rating_score=t.xpath(".//span[@class='rating_nums']/text()")[0]
        rating_nums=t.xpath(".//tr[@class='item']/td[2]/div[@class='star clearfix']/span[@class='pl']/text()")[0].replace('(','').replace(')','').replace(' ','').replace('\n','')
        produce=t.xpath(".//span[@class='inq']/text()")[0]
        imgurl=t.xpath(".//a/img/@src")[0]
        #print(imgurl)
        #(produce)

        book={'title':'title','author':'author','price':'price','press_time':'press_time',
              'rating_nums':'rating_nums','rating_score':'rating_score','produce':'produce'}
        books.append(book)
        imgurls.append(imgurl)
    return books,imgurls

def downloading(url,book):
    if 'bookposter' in os.listdir("D:\code"):
        pass
    else:
        os.mkdir(r"D:\code\bookposter")
    os.chdir(r'D:\code\bookposter')
    img=requests.request('GET',url).content
    with open(book['title']+'.jpg','wb') as f:
        print('正在下载：%s'%url)
        f.write(img)
if __name__=='__main__':
    url='https://book.douban.com/top250?start=25'
    html=get_html(url)
    books=parse_html(html)[0]
    imgurls=parse_html(html)[1]
    # for i in range(25):
    #      downloading(imgurls[i],books[i])
    # for i in range(25):
    #     with open('book.txt','a') as f:
    #     f.write(books[i]+'\n')
    #     print("图书信息写入成功")
    bookdata=pd.DataFrame(books)
    bookdata.to_csv('book.csv')
    print("图书信息写入成功")
