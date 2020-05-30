s=[]
for i in range(int(input())):
    n,a,b,c=input().split()
    a,b,c=float(a),float(b),float(c)
    s.append([n,(a+b+c)/3])
stu=input()
for j in s:
    if j[0]==stu:
        print("%.2f" %j[1])
