for _ in range(int(input())):
    n = int(input())
    b = map(int,input().split())
    e,o =0,0
    s =[]
    for i in b:
        if i%2 ==0:
            e+=1
        else:
            o+=1
    for j in range(n):
        if o>0 and j%2 == 1:
            o -=1
            s.append(1)
        elif e>0 and j%2 ==0:
            e-=1
            s.append(1)
        else:
            s.append(0)
    print(sum(s))
