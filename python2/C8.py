# JSON !!!!
'''
import json

json_str = '{ "name" : "qiyue", "age" : 19 }'
stu = json.loads(json_str)
print(stu, type(stu))


print(stu["name"])
print(stu["age"])

from enum  import Enum
from enum import IntEnum,unique

@unique
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.YELLOW.value)
print(VIP.YELLOW.name)


for v in VIP:
    print(v.value, v.name)

'''
# 闭包是由函数及其相关的引用环境组合而成的实体
# (即：闭包=函数+引用环境)
# (想想Erlang的外层函数传入一个参数a, 内层函数依旧传入一个参数b, 内层函数使用a和b, 最后返回内层函数)

def cure_pre():
    a = 25
    def curve(x):
        return a * x * x
    return curve

f = cure_pre()

print(f(2))
print(f(43))

def f1():
    a = 10
    def f2():
        a = 20
        print(a, "1")
    print(a, "2")
    f2()
    print(a, "3")

f1()

print(f.__closure__)




# origin = 0 

def factory(pos):
    def go(step):
        nonlocal pos
        new = pos + step
        pos = new
        return new
    return go

asdwqeq = factory(0)
print(asdwqeq(2))
print(asdwqeq(3))
print(asdwqeq(5))


 

