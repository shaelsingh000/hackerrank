x=10
y=0
z=x
if x<0:
    print("false")
else:
    while z>0:
        y=y*10+(z%10)
        z=z//10
        print(y)
    if x==y:
        print("true")
    else:
        print("false")