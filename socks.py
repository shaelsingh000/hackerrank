import sys
n=int(input())
a=[int(x) for x in input().split()]
dic={}
count=0
for i in a:
    dic[i]=dic.get(i,0)+1
for i,j in dic.items():
    if j>0:
        count+=j//2
print(count)