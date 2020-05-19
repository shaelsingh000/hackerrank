import sys
n,k=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
a.sort()
sum=0
for i in range(n):
    sum+=a[i]
    if k<sum:
        print(i)
        break