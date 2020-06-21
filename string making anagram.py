<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> 89681f03ca62287f384f2aab4787ea9061b931f8
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
<<<<<<< HEAD
>>>>>>> 51e3700... master
=======
>>>>>>> 89681f03ca62287f384f2aab4787ea9061b931f8
print(p+q-c)