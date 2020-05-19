import sys
n=int(input())
a=[]
sum,c=0,0
for i in range(n):
    b=[int(x) for x in input().split()]
    a.append(b)
for i in range(n):
    sum=sum+a[i][i]
while(n>0):
    sum=sum-a[c][n-1]
    c+=1
    n-=1
print(abs(sum))