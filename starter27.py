for _ in range(int(input())):
    b,c = map(int,input().split())
    a = c/b
    for i in range(1,1000):
        x = a*i
        if x == int(x):
            print(int(x))
            break
