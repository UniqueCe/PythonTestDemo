# 匿名函数

def add(x, y):
    return x + y

lambda x, y: x + y

# print(add(1, 2))

d = lambda x, y: x + y
# print(d(1, 9))


# 三元表达式

x = 3
y = 8
d = x if x > y else y
# print(d)


list_x = [1, 2, 3, 4, 5, 6, 7, 8]
rrrrrrrr = map(lambda x : x * x, list_x)
# print(list(rrrrrrrr))


from functools import reduce

list_x = [1, 2, 3, 4, 5, 6, 7, 8]

r =  reduce(lambda x, y: x + y, list_x)
print(r)

asdw = reduce(lambda x, y: x + y, list_x, 23)
print(asdw)