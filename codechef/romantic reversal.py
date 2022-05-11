for _ in range(int(input())):
    n,m = map(int,input().split())
    s = input()
    a=s
    for i in range(m,-1,-1):
        a = a[i-1::-1]+a[i:m]
    a=a+s[m:]
    print(a[m:])