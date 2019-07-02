# 正则表达式！！！
import re

a = "c|c+13+|java|py45667t8hon|oc789|Sw9789ift|j0654543ava"

'''
asd = re.findall("java", a)
print(asd)

asd1 = re.findall('\\d', a)
print(asd1)

asd2 = re.findall("\\D", a)
print(asd2)

s = "asd,qwd,aes,dfd,ass,adw,ads"
r = re.findall('a[^sd][sd]', s)
print(r)


aa = "asdw78sfe!w*&^@#78e!@rge878werw"
rrNum = re.findall('[0-9]', aa)
rr = re.findall('[^0-9]', aa)
print(rr,"\n",rrNum)
w = re.findall('\\w', aa)
print(w)
WW = re.findall('\\W', aa)
print(WW)
qqq = re.findall('!', aa)
print(qqq)

qweq = "python php java123objc"
qwe = re.findall('[a-z]{3,6}', qweq)
print(qwe)

aaaaaa = "pytho0python1pythonn2"
rrrr1 = re.findall('python*', aaaaaa)
print(rrrr1)
rrrr = re.findall('python+', aaaaaa)
print(rrrr)
rrrr3 = re.findall('python?', aaaaaa)
print(rrrr3)

qq = "1233405134567"
rq = re.findall('^\\d{4,8}$', qq)
print(rq)

qqpy = "pythonpythonpythonpythonpythonpythonpythonpythonpython"
rqpy = re.findall('(python){3}', qqpy)
print(rqpy)


lam = "C#pythonPhp"
r = re.findall('c#', lam, re.I | re.S)
print(r)
lam1 = "C#\npythonPhp"
r1 = re.findall('c#.{1}', lam, re.I | re.S)
print(r1)



def conv(value):
    mat = value.group()
    return '##' + mat + '90'

lam1 = "88C#pythonC#PhpC#"
r1 = re.sub('C#', conv, lam1)
print(r1)

# la = lam1.replace('C#', 'GO')
# print(la)


def conv2(Value):
    mat = Value.group()
    if int(mat) > 56:
        return '-9-'
    else:
        return '<0>'

laaaa = "A678632SDFD676D82384GSGD2HJGJH"        
reaaa = re.sub('\\d{2}', conv2, laaaa)
print(reaaa)

mat = re.match('\\d', laaaa)
print(mat)

mat2 = re.search('\\d', laaaa)
print(mat2)

'''

s = "life is shaort, i use python"
r = re.search('life(.*)python', s)
rqa = re.findall('life(.*)python', s)
print(r,"\n" ,r.group(1))
print(rqa)

