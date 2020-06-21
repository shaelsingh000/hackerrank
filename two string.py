<<<<<<< HEAD
<<<<<<< HEAD
import sys
n=int(input())
a=[input() for i in range(2*n)]
i=0
while i<=(2*n-2):
    for j in a[i]:
        if j in a[i+1]:
            print("YES")
            break
    else:
        print("NO")
=======
=======
>>>>>>> 89681f03ca62287f384f2aab4787ea9061b931f8
import sys
n=int(input())
a=[input() for i in range(2*n)]
i=0
while i<=(2*n-2):
    for j in a[i]:
        if j in a[i+1]:
            print("YES")
            break
    else:
        print("NO")
<<<<<<< HEAD
>>>>>>> 51e3700... master
=======
>>>>>>> 89681f03ca62287f384f2aab4787ea9061b931f8
    i+=2