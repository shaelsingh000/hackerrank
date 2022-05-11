for _ in range(int(input())):
    n,a,b = int(input()),1,2
    while(a|b)<=n:a|=b;b*=2;
    print(1 if not n else b)