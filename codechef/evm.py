for _ in range(int(input())):
    a,b,c,p,q,r=map(int,input().split())
    half = (p+q+r)/2
    print(half)
    hack = max((p-a),(q-b),(r-c))
    print(hack)
    new=a+b+c+hack
    print(new)
    if new>half:
        print("YES")
    else:
        print("NO")