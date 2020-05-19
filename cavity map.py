import sys
n=int(input())
a=[]
for i in range(n):
    b=[x for x in input()]
    a.append(b)
for i in range(1,n-1):
    for j in range(1,n-1):
        if a[i][j]>a[i-1][j] and a[i][j]>a[i+1][j] and a[i][j]>a[i][j-1] and a[i][j]>a[i][j+1]:
            a[i][j]='X'
for i in range(n):
    for j in range(n):
        print(a[i][j],end='')
    print()