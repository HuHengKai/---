import requests
from lxml import etree

headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
urls=['https://www.jiuwa.net/face/p-{}'.format(str(i)) for i in range(10)]
path=r'C:\Users\hu\Desktop\img\ '
def get_image(url):
    data=requests.get(url,headers=headers)
    seletor=etree.HTML(data.text)
    img_urls=seletor.xpath('//div[@class="face-gg"]/p[1]/img/@src')
    for img_url in img_urls:
        data=requests.get(img_url,headers=headers)
        with open(path+img_url[-8:],'wb') as f:
            f.write(data.content)
            f.close()
    print('下载完成')
if __name__ == '__main__':

     for url in urls:
         get_image(url)