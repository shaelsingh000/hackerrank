import sys
b=[]
for i in range(6):
    a=[]
    a=[int(x) for x in input().split()]
    b.append(a)
a=[]
for i in range(4):
    for j in range(4):
        sum=b[i][j]+b[i][j+1]+b[i][j+2]+b[i+1][j+1]+b[i+2][j]+b[i+2][j+1]+b[i+2][j+2]
        a.append(sum)
print(max(a))