import requests
import re
import json
import os
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
#获取url
def get_image_url():
    # print("dd")
    lol_js = requests.get("https://lol.qq.com/biz/hero/champion.js").text
    # print(lol_js)
    reg = r'"keys":(.*?),"data"'
    data = re.findall(reg, lol_js)
    dict_js = json.loads((data[0]))
    print(dict_js)
    return dict_js
# 拼接url
def append_url(dict_js):
    pic_list=[]
    for hero_id in dict_js:
        for i in range(20):
            i=str(i)
            if len(i)==1:
                her_num="00"+i
            elif len(i)==2:
                her_num="0"+i
            nums=hero_id+her_num
            urls='http://ossweb-img.qq.com/images/lol/web201310/skin/big'+nums+'.jpg'
            pic_list.append(urls)
    return pic_list
def path():
 if 'lolimage' in os.listdir("D:\code"):
    pass
 else:
     os.mkdir(r"D:\code\lolimage")
def download(dict_js):
    list_filepath = []
    path = 'D:\cheshi\lolimafes\\'
    for names in dict_js.values():
        # print(names)
        for i in range(20):
            filter_path = path + str(i) + names + '.jpg'
            list_filepath.append(filter_path)
            # print(list_filepath)
    return list_filepath
def downmoad_image(pic_list ,list_filepath):
    n = 0
    for i in pic_list:
        res = requests.get(i)
        print(res)
        # print(res)
        n += 1
        # print(res)
        if res.status_code == 200:
            print("200")
            print("正在下载:%s" % list_filepath[n])
            with open(list_filepath[n], 'wb') as f:
                f.write(res.content)
if __name__=="__main__":
    dict_js=get_image_url()
    pic_list=append_url(dict_js)
    list_filepath=download(dict_js)
    downmoad_image(pic_list,list_filepath)
