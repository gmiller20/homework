n = int(input())
s = input().split()
sp = []
sp.append(s[-1])
for i in s[:-1]:
    sp.append(i)
print(sp)