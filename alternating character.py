import sys
n=int(input())
for i in range(n):
    a=list(input())
    i=0
    d=0
    while i<(len(a)-1):
        if a[i]==a[i+1]:
            a.pop(i+1)
            d+=1
        else:
            i+=1
    print(d)