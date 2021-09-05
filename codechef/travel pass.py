for _ in range(int(input())):
    n,a,b = map(int,input().split())
    s=input()
    p=0
    for i in s:
        if i=='0':
            p+=a
        else:
            p+=b
    print(p)