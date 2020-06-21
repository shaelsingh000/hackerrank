<<<<<<< HEAD
<<<<<<< HEAD
from collections import Counter
n,m=input().split()
n,m=int(n),int(m)
magzine=(x for x in input().split())
note=(x for x in input().split())
if Counter(note)-Counter(magzine)=={}:
    print("YES")
else:
=======
=======
>>>>>>> 89681f03ca62287f384f2aab4787ea9061b931f8
from collections import Counter
n,m=input().split()
n,m=int(n),int(m)
magzine=(x for x in input().split())
note=(x for x in input().split())
if Counter(note)-Counter(magzine)=={}:
    print("YES")
else:
<<<<<<< HEAD
>>>>>>> 51e3700... master
=======
>>>>>>> 89681f03ca62287f384f2aab4787ea9061b931f8
    print("NO")