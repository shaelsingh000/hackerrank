for _ in range(int(input())):
    x,y=map(int,input().split())
    if x==0:
        print("Liquid")
    elif y==0:
        print("Solid")
    else:
        print("Solution")