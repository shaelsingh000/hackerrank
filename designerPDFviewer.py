import sys
a=[int(x) for x in input().split()]
s=[a[ord(c)-ord('a')] for c in input()]
print(max(s)*len(s))