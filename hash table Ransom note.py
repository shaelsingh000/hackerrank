from collections import Counter
n,m=input().split()
n,m=int(n),int(m)
magzine=(x for x in input().split())
note=(x for x in input().split())
if Counter(note)-Counter(magzine)=={}:
    print("YES")
else:
    print("NO")