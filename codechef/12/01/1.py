for _ in range(int(input())):
    a=sum(list(map(int,input().split())))
    b=sum(list(map(int,input().split())))
    c=sum(list(map(int,input().split())))
    print(max(a,b,c))