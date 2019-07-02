
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print ("False")

ore = "asd"
print(ore)

print("asdwadavf\ndasdasd",ore)


num = 12313123
numFloat = 23.34343
numStr = "string"

print(num,numFloat,numStr)
print("保留两位小数",'%.2f' %numFloat,"你擦含税单价回复会计师")
print('%s %s%s'%("白柳喜爱书",'%.2f' %numFloat,"asd"))

array = ["asdas","asdadwww",23,"23.45"]
print("这是数组 - 列表",array,array[1])

arrya = ("asda",123,"asdqwdwvwvw")
print("这是元组",arrya)

# dict = {"key1":"vale1","key2":"vale3"}
# print("这是字典",dict)

aaa = 1234
print(repr(aaa).__class__,str(aaa).__class__)

a = 5
b = 4
c = a*b #(2的4次方)

if c <= 8:
    print("----")
elif c > 30 :
    print("+++")
else:
    print("=====")
print(c)

点 = "的防守打法"
去 = ["阿金石可镂附近的","的防守打法","似懂非懂是"]

if (点 in 去):
    print("OK")
else:
    print("NO")


numnum = 22

if numnum >= 10 and numnum < 20:
    print("OK+++")
else:
    print("____")


if numnum > 10:
    print("asd")
elif numnum == 111:
    print("numnum == 111")
else:
    print("0000")


if numnum == 22: print("num = 22")

print ("My name is %s and weight is %.2f kg!" % ('Zara', 21.2366))

ooo = []
ooo.append("qwe")
ooo.append("iou")
ooo.append(12)
print(ooo)
del ooo[2]
ooo.append(2345)
print(len(ooo))

'''
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")
'''

for i in range(5):
    print(i)

for ii in range(12,19):
    print(ii)

def printStr():
    print("test 一下 ")

printStr()

def 方法名(int):
    print("jghkjl;",int)

方法名(2)


def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

area(23,30)
print_welcome("name")

#
def jisuan(a:int,b:int,str:[str]):
    strStr = "haha %s"%(str)
    print(strStr,a + b - a)

# jisuan(12,2,"name")
# jisuan(a = 12, b = 12, str = "asd")
jisuan(12,22,["asd","qwe"])


a = 10
def test():
    global a
    a = a + a + 111
    print(a)
test()

qqqqq = ["啊啊啊","待付款","斯柯达","积分","设计费","束带结发","不不不","发方法"]
wwwww = [123,3454,456,567675,2342342423,235,1,34]
qqqqq.sort()
wwwww.sort()
print(qqqqq)
print(wwwww)


def ChangeInt( a ):
    print(a)
    a = 10

b = 2
ChangeInt(b)
print( b ) # 结果是 2

print("---------")


bqq = 19

def changeNum(bb:int):
    print(bb)
    bb += 10
    print(bb)
    return bb

print(changeNum(bqq),bqq)

print("---bb------")

def changeNumaa(bb:int,qqqqq:str,cc:float):
    print(bb)
    bb += 10
    print(bb,qqqqq,'%.2f'%cc)

changeNumaa(bqq,"asdq",12.345)
print(bqq)

def test00(int,str,float):

    int += 10
    str += "asdw"

    print(int,str,float)

test00(123,"asdw",12.3455)

test00(int=123244,str="1231",float=1234.569)


def testDef(num:int,zfc:str,fuDian:float):
    print(num,zfc,'%.2f'%fuDian)

testDef(12,"字符串",123.45)


qweqwe:str = 123.234
qwerty:str = "史蒂芬霍金"
qwertyrty:int = "是否是开户费看数据"
qwertyrty = "是否是开户费看数据"
print(repr(qweqwe).__class__,qweqwe,
      repr(qwerty).__class__,qwerty,
      repr(qwertyrty).__class__,qwertyrty,
      float(qweqwe));


def tesTDef23(zfc:str,num:int = 123,asd:int = 122223):
    print("======")
    print(num,zfc,asd)

tesTDef23("字符串")
tesTDef23("123",num=123,asd=456)


dictTest = {"key1":"value","key2":123,"key3":"daqqq"}

for k,v in dictTest.items():
    print(k,v)

print(dictTest)

'''
f = open("/Users/lzhl_ios/Desktop/test.txt","w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
f.close()

b = open("/Users/lzhl_ios/Desktop/test.txt","r")
aa = b.read()
print(aa)
print("==================================")

import os,sys,random

ret = os.access("/Users/lzhl_ios/Desktop/test.txt", os.F_OK)
print ("F_OK - 返回值 %s"% ret)

'''
import os,sys,random

print("--------------------------------")

class people:
    name = ""
    age = 0

    def __init__(self,n,a):
        self.name = n
        self.age = a

    def speak(self):
        print("%s 说: 我 %d 岁" % (self.name,self.age))


p = people("石磊",123)
p.speak()

print(random.randrange(12))


# from datetime import  date

import  calendar

cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print(cal)

# 九九乘法表

for i in range(1, 10):
    for j in range(1, i+1):
        # print('{}x{}={}\t'.format(i, j, i*j), end='')
        print("%dx%d=%d\t"%(i,j,i*j),end='')
    print()


import json

# Python 字典类型转换为 JSON 对象
data = {
        'no' : 1,
        'name' : 'Runoob',
        'url' : 'http://www.runoob.com'
        }

json_str = json.dumps(data)
print ("JSON 对象：", json_str,repr(json_str.__class__))


json_str_json = json.loads(json_str)
print(json_str_json,json_str_json['name'])



def test1233(dic:dict):
    print(dic,repr(dic).__class__)

test1233({"name":"sda"})
test1233("name")

import time

# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

q = ["123","13242","asd"]
it = iter(q)
print(next(it))

'''
while True:
    try:
        print(next(it))
    except StopIteration:
        print("结束")
        break

'''

for i in q:
    print(next(it))
