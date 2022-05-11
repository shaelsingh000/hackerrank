from collections import Counter
for _ in range(int(input())):
    n= int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    z = Counter(x+y)
    ele = list(z.keys())[list(z.values()).index(max(list(z.values())))]
    count = 0
    if x == y:
        print(count)
    else:
        for i in zip(x,y):
            k = 0
            if i[0]==i[1] and i[0] == ele:
                pass
            elif i[1] == ele and i[0] != ele:
                count +=1
            elif i[0] == ele and i[1] != ele:
                count +=1
                
            elif i[0]==i[1] and i[0]!=ele:
                count +=1
            elif i[0] != i[1]:
                k = ele-i[0]
                a = i[0]+k
                b = i[1]-k
                if a==b:
                    count+=1
                elif a!=b:
                    count+=2
            else:
                pass
    print(count)
