from collections import deque
d=deque()
for _ in range(int(input())):
    a=input().split()
    getattr(d, a[0])(*[a[1]] if len(a) > 1 else [])
print(*d)
