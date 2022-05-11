from re import A

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    if (a[0]==n) & (a[0]==b[1]) & (a[0]==c[2]):
        print("0")
    else:
        print(a[1]+a[2]+b[2])