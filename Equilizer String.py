n = int(input())
x = list(input())
y = list(input())
c = 0
for i in range(len(x)-1):
    if(x[i]!=y[i]):
        if(x[i]==y[i+1]):
            x[i],x[i+1]=x[i+1],x[i]
            c+=1
        elif(x[i]=='0'):
            x[i]='1'
            c+=1
        elif(x[i]=='1'):
            x[i]='0'
            c+=1
    
if(x[len(x)-1]!=y[len(x)-1]):
        c+=1
print(c)
        