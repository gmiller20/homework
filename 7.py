x = int(input())
a = int(input())
b = int(input())
if a >= x and b >= x:
    print(2)
elif a >= x and b < x:
    print('Mike')
elif a < x and b >= x:
    print('Ivan')
elif (a + b) >= x and a < x and b < x:
    print(1)
else:
    print(0)
1