a = list(map(int,input().split(",")))
a.sort()
b = []
count = 0
for i in range(len(a)):
    try:
        if a[i]+1 == a[i+1]:
            count=count+1
        else:
            if count>0:
                b.append(count+1)
                count=0
    except:
        pass
if len(b)==0:
    print(-1)
else:
    print((b))