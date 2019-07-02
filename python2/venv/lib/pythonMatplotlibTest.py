
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    print("OK")
'''
# 绘制图形
data = np.arange(0,100)
plt.subplot(211)
plt.plot(data)

data2 = np.arange(100,250)
# plt.figure()
plt.subplot(2,1,2)
plt.plot(data2)

plt.show()
'''


'''
# 线条的几种形式
plt.plot([1, 1.5, 2, 2.5, 3], [3, 4, 6, 7, 9], ':rs')
plt.plot([0, 1.75, 2.5, 3], [2, 4, 5 , 7.5], '-.g')
plt.plot([0.5, 2, 3], [2, 5, 8], '--g^')
plt.plot([1.5, 1.8, 3], [2, 4, 6.5], 'go-')

plt.show()

'''

'''
# 散点图
N:int = 20

# filled_markers = ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')
plt.scatter(np.random.rand(N) * 100,
           np.random.rand(N) * 100,
           c='r', s=500, alpha=0.5, linewidths=5, edgecolors='b',
            marker='*')


plt.scatter(np.random.rand(N) * 100,
           np.random.rand(N) * 100,
           c='g', s=250, alpha=0.5,
            marker='D')


plt.scatter(np.random.rand(N) * 100,
           np.random.rand(N) * 100,
           c='y', s=400, alpha=0.5,
            marker='o')

plt.show()
'''


'''
# 饼状图
labels = ["Mon", "Tue", "Web", "Thu", "Fri", "Sat", "Sun"]
data = np.random.rand(7) * 100
plt.pie(data, labels=labels, autopct='%2.2f%%')
plt.axis('equal')
plt.legend(loc='upper center', bbox_to_anchor=(1, 1), ncol=1, shadow=True)
# 上面bbox_to_anchor被赋予的二元组中，第一个数值用于控制legend的左右移动，
# 值越大越向右边移动，第二个数值用于控制legend的上下移动，值越大，越向上移动。 

plt.show()
'''


'''
# 条形图
N:int = 7
x = np.arange(N)
data = np.random.randint(low=0, high=100, size=N)
colors = np.random.rand(N * 3).reshape(N, -1)
labels = ["Mon", "Tue", "Web", "Thu", "Fri", "Sat", "Sun"]

plt.title("Weekday Data")
plt.bar(x, data, alpha=0.8, color=colors, tick_label=labels)
plt.show()
'''






