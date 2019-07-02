import teqw


#coding: utf-8


def main():
    print("开始了！！！")

if __name__ == '__main__':
    main()

'''
print("please input user_name")
user_name = "AS"
user_name = str(user_name)
print(user_name,type(user_name))

print("please input user_password")
user_password = "12"
print(user_password)

if user_password == "asdw" and user_name == "123": 
    print("success")
else:
    print("fial")
'''
# if 1:
#     print("asdasda")
# else:
#     print("asdsadsad")

num = 1

# while num <= 10:
#     num += 1
#     print(num)

while num <= 10:
    num += 1
    print(num,end=', ')
else:
    print("num = 10 ")

for  x  in range(10,0,-2): 
    print(x, end=" | ")


a = [1,2,3,4,5,6,7,8,9]

b = a[0:len(a):2]
print(b)

aa = "asdada"
print('吃' + aa)
print(teqw.abs)


@classmethod
def asdw_asd(cls):
    print('-classmenthod-')




