from collections import Counter
n = int(input())
for _ in range(n):
    s= input()
    l= len()
    if len(s) % 2 != 0:
        print("-1")
    else:
        print(sum((Counter(s[:l//2]) - Counter(s[l//2:])).values()))