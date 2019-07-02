
import requests,re,tkinter
from bs4 import BeautifulSoup


# 爬取小说！！！
name = input("请输入小说名称：")

def noAdvertisingNovel(url: str, biaoQian: str):
    req = requests.get(url=url)
    df = BeautifulSoup(req.text, 'html.parser')
    texts = df.find_all(biaoQian)
    return texts


target = "https://www.biquge5200.com/modules/article/search.php?searchkey=" + name
'''
req = requests.get(url=target)
df = BeautifulSoup(req.text,'html.parser')
texts = df.find_all('a')
'''
texts = noAdvertisingNovel(target,'a')


# 检索到包含用户输入小说名称的地址
nameUrl = ""
for k in texts:
    if k.text == name:
        nameUrl = k['href']
        break
    else:
        pass

'''
req2 = requests.get(url=nameUrl)
df2 = BeautifulSoup(req2.text,'html.parser')
texts2 = df2.find_all('a')
'''
texts2 = noAdvertisingNovel(nameUrl,'a')

tempUrl = ""
for k in texts2:
    matchObj = re.match('第一章', k.text)
    if matchObj:
        tempUrl = k['href']
        break
    else:
        pass

req3 = requests.get(url=tempUrl)
df3 = BeautifulSoup(req3.text,'html.parser')
texts3 = df3.find_all('div',id='content')

print(texts3[0].text,'\n')

tempNextUrl = tempUrl
# arr = re.match('[a-zA-z]+://[^s]*',tempUrl)
# tempGroup = re.match('(\w+)://([^/:]+)(:\d*)?([^# ]*)', arr.group())

nextNum = int(tempUrl[36:44]) + 1
# 下一张的Url
nextUrl = tempUrl[0:35] + '/%d'%nextNum + '.html'

print("next",nextUrl)


