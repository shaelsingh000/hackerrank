n,m=map(int,input().split())
r=[list(map(int,input().split())) for i in range(n)]
k=int(input())
for i in sorted(r, key = lambda r: r[k]):
    print(*i)