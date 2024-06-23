s = input()
gl = 0
sogl = 0
for i in s:
    if i in 'aeiou':
        gl += 1
    else:
        sogl += 1
print(sogl)
print(gl)
a = 0
e = 0
i1 = 0
o = 0
u = 0
for i in s:
    if i == 'a':
        a += 1
    if i == 'e':
        e += 1
    if i == 'i':
        i1 += 1
    if i == 'o':
        o += 1
    if i == 'u':
        u += 1
print('a -', a)
print('i -', i1)
print('e -', e)
print('o -', o)
print('u -', u)