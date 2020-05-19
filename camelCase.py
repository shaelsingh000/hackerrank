import sys
s=input()
c=0
for i in s:
    if ord(i)>64 and ord(i)<91:
        c+=1
print(c+1)