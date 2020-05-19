import sys
n,m=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
a.sort()
sum1=[]
for i in range(len(a)//m):
    sum2=[]
    for j in range(m):
        sum2.append(a[0])
        a.remove(a[0])
    sum1.append(sum(sum2)*(i+1))
print(sum(sum1)+(sum(a)*(i+1)))