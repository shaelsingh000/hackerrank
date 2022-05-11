from matplotlib import collections


from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = Counter(a)
    x,y=0,0
    for key, value in b.items():
        if 1==value:
            x=key
            break
    for i in range(2*n):
        print(i)
        if i not in a:
            y = i
            break
    if x<y:
        print("NO")
    else:
        print(x,y)
