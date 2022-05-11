for _ in range(int(input())):
    n = int(input())
    a,b = [],[]
    for _ in range(n):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    a = set(a)
    b = set(b)
    print(len(a)+len(b))
