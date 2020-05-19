import sys
n=int(input())
a=[int(x) for x in input().split()]
count,temp=0,0
for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            count+=1
print("Array is sorted in",count,"swaps.")
print("First Element:",a[0])
print(a)
print("Last Element:",a[n-1])  