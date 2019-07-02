print("12%")
print(3/4.0)
print(4.0/3)

my_a = 'asda'
print(f"Let't table {my_a}.")
print("s - Let't table %s."% my_a)
print(round(4/3))
print(round(5/3))

a = 'asd-{}'
print(a.format('111'))
print('asdadasda-',my_a)

print('How old are you?',end='')
age = input()

print(f"you're {age} old !")

def main():
    pass

if __name__ == '__main__':
    main()

from sys import argv


# 读取文件！！！！
file_again = input(">")
text_again = open(file_again)
print(text_again.read())