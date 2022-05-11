for _ in range(int(input())):
    n,m = map(int,input().split())
    if n>=m:
        print(m)
    else:
        a=m%n
        print(a-1)