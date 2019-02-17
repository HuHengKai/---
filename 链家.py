import os
import requests
from lxml import etree
import pymysql
#连接数据库,数据库操作
db=pymysql.Connect(host='localhost',port=3306,user='root',
                   passwd='123456',db='tushu', charset='utf8'
                   )
cursor=db.cursor()
urls=['https://bj.lianjia.com/ershoufang/pg{}/'.format(str(i)) for i in range(2,4)]
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
            #print(html.text)
    except Exception as f:
        print("获取失败")
    return html.text
def parser(html):
    html=etree.HTML(html)
    titles=html.xpath("//div[@class='address']/div[@class='houseInfo']/a/text()")
    daxiao=html.xpath("//div[@class='address']/div[@class='houseInfo']/text()[1]")
    price=html.xpath("//div[@class='priceInfo']/div[@class='totalPrice']/span/text()")
    images=html.xpath("//a[@class='noresultRecommend img ']/img[@class='lj-lazy']/@src")
    age=html.xpath("//div[@class='info clear']/div[@class='flood']/div[@class='positionInfo']/text()[2]")
    print(age)
    #插入数据库
    for i in range(0,len(age)):
        cursor.execute('insert into rooms(`title`,`daxiao`,`price`,`age`,`image`) value("{}","{}","{}","{}","{}") '.
                       format(titles[i],daxiao[i],price[i],age[i],images[i]))
        db.commit()
        print("正在存储%s:"%titles[i])
        # cursor.commit()
        # cursor.execute('''insert into rooms(`title`,`daxiao`,`price`,`image`,`age`) value("{}","{}","{}"."{}","{}") '''.
        #                format(titles[i], daxiao[i], price[i], pymysql.escape_string(images[i]), age[i]))
        # cursor.commit()



if __name__=='__main__':
    for url in urls:
        html = get_html(url)
        parser(html)
    # html=get_html(url)
    # parser(html)





