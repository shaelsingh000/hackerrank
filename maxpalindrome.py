import sys
n,k=[int(x) for x in input().split()]
s=list(input())
a=s[::-1]
for i in range(len(a)):
    if k>0:
        if s==a and k>1:
            for j in range(len(a)):
                s[-(j+1)]=9
                s[j]=9
                k-=2
        elif s==a and k==1:
            s[len(a)//2+1]=9
        elif s[i]==a[i]:
            pass
        elif s[i]>a[i]:
            s[-(i+1)]=s[i]
            k-=1
        elif s[i]<a[i]:
            s[i]=a[i]
            k-=1
if s==s[::-1]:
    print(''.join(s))
else:
    print("-1")