for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    x=a+b+c
    y=a+b
    if x<=d:
        print("1")
    elif y<=d:
        print("2")
    else:
        print("3")