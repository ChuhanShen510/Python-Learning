i = 1
while i < 9:
    i += 1
    if i % 2 == 0 and i != 2:
        print(i, '=', '2', '*', i / 2)
    else:
        if i % 3 == 0 and i != 3:
            print(i, '=', '3', '*', i / 3)
        else:
            print(i, '是一个素数')
