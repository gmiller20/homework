s = input()
sp = []
for i in range(len(s)):
    if s[i] == ' ' and s[i] == s[i + 1]:
        continue
    else:
        sp.append(s[i])
print("".join(sp))