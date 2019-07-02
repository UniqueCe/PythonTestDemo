import time

def timeF():
    # print(time.time())
    return time.time()


tempT =  timeF()
t = time.localtime(tempT)
dt = time.strftime("%Y-%m-%d %H:%M:%S",t)
dt2 = time.strftime("%Y年%m月%d日 %H:%M:%S",t)
# print(dt)
# print(dt2)


def print_time(asda):
    print(time.time())
    asda()

def f2():
    print("asd")

def f3():
    print("asd33")

# print_time(f2)
# print_time(f3)


#装饰器
def decorator(func):
    def wea():
        print(time.time())
        tempT =  timeF()
        t = time.localtime(tempT)
        dt = time.strftime("%Y-%m-%d %H:%M:%S",t)
        dt2 = time.strftime("%Y年%m月%d日 %H:%M:%S",t)
        print(dt)
        print(dt2)
        func()
    return wea

ff = decorator(f2)
ff()

print("---------")

@decorator
def f4():
    print("asd33")


f4()



str = "\n             asdadad"
print (str.strip()) 
