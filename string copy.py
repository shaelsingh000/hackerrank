import sys
n=int(input())
s=[]
for i in range(n):
    s.append(set(input()))
for i in s:
    print(len(i))