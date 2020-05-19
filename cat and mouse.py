import sys
n=int(input())
b=[]
for i in range(n):
    a=[]
    a=[int(x) for x in input().split()]
    b.append(a)
for i in range(n):
    if abs(b[i][0]-b[i][2])<abs(b[i][1]-b[i][2]):
        print("Cat A")
    elif abs(b[i][0]-b[i][2])>abs(b[i][1]-b[i][2]):
        print("Cat B")
    elif abs(b[i][0]-b[i][2])==abs(b[i][1]-b[i][2]):
        print("Mouse C")