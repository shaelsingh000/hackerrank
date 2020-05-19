import sys
import collections
s1=collections.Counter(input().strip())
s2=collections.Counter(input().strip())
count=0
for i in s1.keys():
    if i in s2.keys():
        print(s1)
        print(s2)
        print(i)
        print(min(s1[i],s2[i]))
        count+=min(s1[i],s2[i])
print(count)