a = int(input())
if a % 2 == 0 and a < 0:
    print('отрицательное четное число')
elif a == 0:
    print('нулевое число')
elif a % 2 == 0 and a > 0:
    print('положительное четное число')
else:
    print('число не является четным')