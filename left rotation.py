import sys
n,d=[int(x) for x in input().split()]
a=[int(i) for i in input().split()]
for i in range(d):
    b=a.pop(0)
    a.append(b)
for i in a:
    print(i,end=" ")