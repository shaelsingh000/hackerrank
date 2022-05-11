for _ in range(int(input())):
    x,y=input().split()
    flag=0
    s,t="",""
    if y not in x:
        print(0)
    else:
        for i in x:
            if flag==0 and i==y:
                s=str(int(i)+1)
                flag=1
                t=t+i
            elif flag==1 and y!='0':
                s=s+'0'
                t=t+i
            elif flag==1 and y=='0':
                s=s+'1'
                t=t+i
        s,t=int(s),int(t)
        print(s-t)
