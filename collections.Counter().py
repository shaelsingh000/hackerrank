from collections import Counter as c
x,a=int(input()),[int(i) for i in input().split()]
a=c(a)
n=int(input())
sum=0
for _ in range(n):
    p,q=map(int,input().split())
    if p in a.keys():
        if a[p]>0:
            sum+=q
            a[p]-=1
print(sum)