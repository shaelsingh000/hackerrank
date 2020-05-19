from collections import Counter
n=int(input())
s=input().lower()
q=int(input())
a=[]
for i in range(q):
    b=[int(x) for x in input().split()]
    a.append(b)
for i in a:
   f=Counter(s[i[0]:(i[1]+1)])
   print(f[max(f.keys())])