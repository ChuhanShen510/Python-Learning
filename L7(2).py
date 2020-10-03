import random
x = range(1, 31)
y = range(1, 16)
print('开奖结果是：', random.choices(x, k=6))
print('特别号码是：', random.choices(y, k=1))
