import requests
import pprint
import re
from pyquery import PyQuery
#拼接
from urllib.parse import urlencode
import pymysql
#连接数据库,数据库操作
db=pymysql.Connect(host='localhost',port=3306,user='root',
                   passwd='123456',db='tushu', charset='utf8mb4'
                   )
cursor=db.cursor()
base_url="https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0&"
#获取页面,请求的方法
def get_page(page):
        prames= {
                 # "page_type": "03",
                 "page":page,
                 # "汉字":"汉字"
                 }
        # print(base_url+urlencode(prames))
        response=requests.get(base_url+urlencode(prames))
        # print(response)
        return response.json()
        print(response.json)
        # return response.json()
        # print(response.json())
        # pprint.pprint(response.json())
#解析数据
def prase_data(res_json):
    #print(res_json)
     # pprint.pprint(res_json["data"]["cards"])
    # for i in res_json["data"]["cards"]:
    #     print(i["mblog"]["text"])
    for item in res_json["data"]["cards"]:
        source_time=item["mblog"]["created_at"]
        photo = item["mblog"]["source"]
        # name=item["source"]
        id = PyQuery(item["mblog"]["id"]).text()
        text = PyQuery(item["mblog"]["text"]).text()
        print(text)
        source_place= item["mblog"]["user"]["screen_name"]
        cursor.execute('insert into weibo2(`id2`,`place`,`photo`,`time`,`text`) value("{}","{}","{}","{}","{}") '.
                       format(id, source_place,photo,source_time,pymysql.escape_string(text)))
        db.commit()
        print("正在保存%s"%source_place)
        # print(id,text,source_place,source_time,photo)
        # print(type(text))
        #print(text)
        # result1 = re.findall('((\w*.?).?\w*)<span class="url-icon">', text, re.S)
        # result2 = re.findall('#(.*?)\#', text, re.S)
        # #print(type(result1))
        # result3 = re.findall('<span class="surl-text">(\w*)</span', text, re.S)
        # print(result1,result2,result3)
        #print(id,photo,source,text)
        # text = item["mblog"]["text"]
        # id=item["mblog"]["id"]
        # print(id)
        # screen_name = item["mblog"]["user"]["screen_name"]
        # cursor.execute('insert into weibo(`id2`,`name`,`text`) value("{}","{}","{}") '.
        #                format(id,screen_name,text))
        # db.commit()
        # print(id, text,screen_name)
if __name__=="__main__":
     for page in range(2,10):

        res_json=get_page(page)

        prase_data(res_json)
