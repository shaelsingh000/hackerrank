import sys
n=int(input())
a=[input() for i in range(2*n)]
i=0
while i<=(2*n-2):
    for j in a[i]:
        if j in a[i+1]:
            print("YES")
            break
    else:
        print("NO")
    i+=2