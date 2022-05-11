a=input()
a = a[1:len(a)-1]
b = []
x = ""
for i in a:
	if i==',':
		b.append(int(x))
		x=""
	else:
		x+=i
n=int(input())
s=0
e=len(b)-1
if b[s]==n:
    print(0)
elif b[e]==n:
    print(e)
else:
    while s<e:
        mid = (s+e)//2
        if b[mid]==n:
            print(mid)
            break
        elif b[mid]<n:
            s= mid+1
        elif b[mid]>n:
            e = mid-1
        else:
            pass
