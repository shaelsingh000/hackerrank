for _ in range(int(input())):
    n,m=map(int,input().split())
    s = list(map(int,input().split()))
    r = {1}
    a = s[0]
    b = s[1]
    flag = 0
    s.sort()
    for i in s:
        r.add(i)
    for i in s:
        for j in s:
            if i*j<=m:
                r.add(i*j)
            else:
                break
    for i in s:
        for j in s:
            for k in s:
                if i*j*k<=m:
                    r.add(i*j*k)
                else:
                    break
    print(len(r))
    
