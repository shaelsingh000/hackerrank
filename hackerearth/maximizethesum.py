for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    result = []
    i = 1
    while(i<=k):
        result.append(a[i-1])
        if a[i-1]==a[i]:
            k+=1
        i+=1
    print(sum(result))
