<<<<<<< HEAD
<<<<<<< HEAD
from collections import Counter
n = int(input())
for _ in range(n):
    s= input()
    l= len()
    if len(s) % 2 != 0:
        print("-1")
    else:
=======
=======
>>>>>>> 89681f03ca62287f384f2aab4787ea9061b931f8
from collections import Counter
n = int(input())
for _ in range(n):
    s= input()
    l= len()
    if len(s) % 2 != 0:
        print("-1")
    else:
<<<<<<< HEAD
>>>>>>> 51e3700... master
=======
>>>>>>> 89681f03ca62287f384f2aab4787ea9061b931f8
        print(sum((Counter(s[:l//2]) - Counter(s[l//2:])).values()))