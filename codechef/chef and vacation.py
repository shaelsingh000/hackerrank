for _ in range(int(input())):
    a = list(map(int,input().split()))
    if a[0]+a[1]<a[2]:
        print("PLANEBUS")
    elif a[0]+a[1]>a[2]:
        print("TRAIN")
    else:
        print("EQUAL")