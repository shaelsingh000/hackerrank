import random
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    sum = []
    
    temp = a[:]
    for  i in range(len(temp)-1,0,-1):
        randomidx = random.randint(0,i+1)
        temp[randomidx],temp[i] = temp[i],temp[randomidx]
        print(temp)
        count = 0
        for j in range(n):
            count += (temp[j]+j+1)%2
        sum.append(count)
    print(max(sum))