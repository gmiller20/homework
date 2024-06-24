a = int(input())
ed = a % 10
des = a // 10 % 10
sot = a // 100 % 10
tis = a // 1000 % 10
destis = a //10000 % 10
print(des ** ed * sot / (destis - tis))