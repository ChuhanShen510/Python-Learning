for x in range(1,10):
    for y in range(0,10):
        for z in  range(0,10):
            if 100 * x + 10 * y + z == x ** 3 + y ** 3 + z ** 3:
                print(100 * x + 10 * y + z)