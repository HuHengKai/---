import requests
import re
import pymysql
#连接数据库,数据库操作
db=pymysql.Connect(host='localhost',port=3306,user='root',
                   passwd='123456',db='db', charset='utf8'
                   )
cursor=db.cursor()
#cursor.execute('select * from images')
#print(cursor.fetchall())
#小驼峰
#获取图片列表
def getImagesList(page):
    #获取斗图网源代码.text获取源代码,不加text获取的为状态码
    html=requests.get('http://www.doutula.com/photo/list/?page={}'.format(page)).text
    '''data-original="http://img.doutula.com/production/uploads/image//2019/02/04/20190204293815_mHGMcq.gif!dta"
     alt="想" 
     '''
    #正则表达式 通配符 匹配所有()加是得到想要的，不加的不想要的
    reg=r'data-original="(.*?)".*?alt="(.*?)"'
   # print(html)
    #增加匹配效率，S多行匹配
    reg=re.compile(reg,re.S)
    #列表
    imagesList=re.findall(reg,html)
    #元祖
    for i in imagesList:
        #print(i)
        image_url=i[0]
        image_title=i[1]
        cursor.execute("insert into images(`name`,`imageUrl`) values ('{}','{}')"
                       .format(image_title,image_url))
        print('正在保存%s'%image_title)
        db.commit()
    #保存
       # print(image_url)
    #print(imagesList)
    #range范围1=<x<100
for i in range(1,100):
    print('第{}页'.format(i))
    getImagesList(i)