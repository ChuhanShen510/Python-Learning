x = int(input('请输入一个正整数：'))
if x < 0 or x % 10 == 0 and x != 0:
    print('不是回文数')
else:
    revertedNumber = 0
    temp = x
    while temp != 0:
        revertedNumber = revertedNumber * 10 + temp % 10
        temp //= 10

    if x == revertedNumber or x == revertedNumber // 10:
        print("是回文数。")
    else:
        print("不是回文数。")