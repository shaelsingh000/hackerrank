n = int(input())
a = []
r = ""
flag = 0
while n>0:
    a.append(n%10)
    n=n//10
a.sort()
l = len(a)
if l%2==1:
    flag = -1
   
for j in range(0,len(a),2):
    try:
        if a[j] !=a[j+1]:
            flag = -1
    except:
        pass

for i in range(-1,-l,-2):
    r=r+str(a[i])
for i in range(0,len(a),2):
    r=r+str(a[i])
if flag == -1:
    print(-1)
else:
    print(int(r))
    
