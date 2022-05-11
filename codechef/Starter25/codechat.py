for _ in range(int(input())):
    n,m = map(int,input().split())
    n = n//2
    print(min(n,m))