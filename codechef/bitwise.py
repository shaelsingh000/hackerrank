for _ in range(int(input())):
    n = int(input())
    m = list(map(int,input().split()))
    s=0
    for i in range(len(m)):
        t = m[i]
        a,b = i-1,i+1
        while True:
            if a>=0 and b<len(m):
                
            