import sys
from collections import Counter
a=input()
b=input()
p,q=len(a),len(b)
a=Counter(a)
b=Counter(b)
c=0
d=0
for i,j in a.items():
    if i in list(b.keys()):
        d=min(a[i],b[i])*2
        c+=d
print(p+q-c)