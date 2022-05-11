n = int(input())
a=0
m=1
for i in range(1,n+1):
    if i%2==0:
        a+=i
    else:
        m*=i
print("sum is",a,"\n and product is",m)