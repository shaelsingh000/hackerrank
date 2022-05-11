from collections import Counter
n = input()
a = list(map(int,input().split()))
m=max(a)
a = Counter(a)
print(a[m])