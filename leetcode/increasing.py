s="hello world 5 x 5"
s = s.split()
b = []
flag="true"
for i in s:
    if i.isdigit():
        b.append(int(i))
print(b,len(b))
for i in range(len(b)-1):
    if b[i]<b[i+1]:
        flag="true"
        print(1)
    else:
        flag="false"
        print(2)
        break
print(flag)
