for _ in range(int(input())):
    a,b,c,d,e = map(int,input().split())
    flag = 0
    s = [a,b,c]
    s.sort(reverse=True)
    for i in s:
        if i<=e:
            flag+=1
            s.remove(i)
            break

    if sum(s)<=d and flag==1:
        print("YES")
    else:
        print("NO")
