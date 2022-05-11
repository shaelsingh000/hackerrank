 
for _ in range(int(input())):
    x,y = map(int,input().split())
    z = abs(y-x)
    if z%2==1:
        result = (z//2)+2
        print(z)
    else:
        result = z//2
    print(result)