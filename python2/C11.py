# python 使用字典代替switch

switcherDict = {
    0 : 'Sunday',  
    1 : 'Monday',
    2 : 'Tuesday'
}

day_name = switcherDict[0]
print(day_name)
day_name1 = switcherDict.get(5, 'Unkown')
print(day_name1)

# 列表推导式
a = [1,2,3,4,5,6,7,8,9]
b = [i**2 for i in a]
print(b)


student = {
    '老熊': 18,
    '熊二': 19,
    '熊三': 20
}

bb = [key for key,value in student.items()]
print(bb)