from collections import OrderedDict
d=OrderedDict()
for _ in range(int(input())):
    i=input()
    d.setdefault(i,0)
    d[i]+=1
print(len(d))
print(*d.values())
