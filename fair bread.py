import sys
n=int(input())
a=[int(x) for x in input().split()]
c=0
if sum(a)%2!=0:
    print("NO")
else:
    for i in range(n):
        if a[i]%2!=0:
            a[i]+=1
            a[i+1]+=1
            c+=2
    print(c)