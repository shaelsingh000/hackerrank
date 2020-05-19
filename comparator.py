import sys
n=int(input())
a=dict(input().split() for i in range(n))
b=[]
for i in a.values():
    b.append(int(i))
b.sort()
print(b)