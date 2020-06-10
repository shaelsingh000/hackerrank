from collections import OrderedDict
d=OrderedDict()
for _ in range(int(input())):
    i=input().rpartition(" ")
    d[i[0]]=int(i[-1])+d[i[0]] if i[0] in d else int(i[-1])
for item,price in d.items():
    print(item,price)