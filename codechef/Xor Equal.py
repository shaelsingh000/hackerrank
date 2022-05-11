from collections import Counter
for _ in range(int(input())):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    c1 = Counter(a)
    b = list(map(lambda s: s^x,a))
    c2 = Counter(b)
    c3 = Counter(a+b)
    print(c1,c2,c3)
    ele = list(c3.keys())[list(c3.values()).index(max(list(c3.values())))]
    p = c1[ele]
    q = c3[ele]
    print(q,(q-p))
