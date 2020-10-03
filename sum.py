i = 0
x = 0
while i <= 1000000:
    if i % 2 == 0:
        x = i+x
       
    i = i + 1

print('1000000以内所有偶数的和是', x)
