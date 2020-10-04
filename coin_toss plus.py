import random

counts = int(input("请输入抛硬币的次数："))
i = 0
h = 0
t = 0
ma = 0
temp = 0
mi = 0
temp2 = 0

if counts < 100:
    print("开始抛硬币实验：")

    while i < counts:
        num = random.randint(1, 10)

        if num % 2:
            print("正面", end=" ")
            h = h + 1
            temp += 1
            if mi < temp2:
                mi = temp2
            temp2 = 0
        else:
            print("反面", end=" ")
            t = t + 1
            temp2 += 1
            if ma < temp:
                ma = temp
            temp = 0
            
        i = i + 1

    print(\n'正面:', h)
    print('反面:', t)
    print('最多连续正面', ma)
    print('最多连续反面', mi)
    
if counts >= 100:
    print("开始抛硬币实验：")
    while i < counts:
        num = random.randint(1, 10)
        
        if num % 2:
            h = h + 1
            temp += 1
            if mi < temp2:
                mi = temp2
            temp2 = 0
        else:
            t = t + 1
            temp2 += 1
            if ma < temp:
                ma = temp
            temp = 0

        i = i + 1
        
    print('正面:', h)
    print('反面:', t)
    print('最多连续正面', ma)
    print('最多连续反面', mi)
    
