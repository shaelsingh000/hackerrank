for _ in range(int(input())):
    x,y=map(int,input().split())
    if y==0:
        print(x)
    elif x==y:
        print(2*x-1)
    else:
        print((x-y)+2*y)