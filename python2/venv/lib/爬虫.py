
import requests,time
from bs4 import BeautifulSoup


# 爬取小说！！！
'''
target:str = "http://www.biqukan.com/1_1094/5403177.html"
req = requests.get(url=target)
df = BeautifulSoup(req.text,'html.parser')
texts = df.find_all('div',class_ = 'showtxt')
print(texts[0].text.replace('\xa0'*8,'\n\n'))
'''

def theCrawler(message:str ,url:str):

    target:str = "https://gupiao.baidu.com/stock/%s" %url
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    df = BeautifulSoup(req.text,'html.parser')
    stock_info_text = df.find_all('div',class_ = 'price s-down ')

    # print(df)

    if len(stock_info_text) > 0:
        print(message, "跌幅", stock_info_text[0].text)
    else:
        try:
            stock_info_text = df.find_all('div',class_ = 'price s-up ')
            print(message, "涨幅", stock_info_text[0].text)
        except:
            stock_info_text = df.find_all('div', class_= 'error-page')
            print(message,stock_info_text[0].text)


while True:
    theCrawler(message="上证指数",url="sh000001.html?from=aladingpc")
    theCrawler(message="精工钢构",url="sh600496.html")
    theCrawler(message="莱茵体育", url="sz000558.html")
    theCrawler(message="纳斯达克", url="us@CCO.html?from=aladingpc")
    time.sleep(60)
    print("-----------------")


