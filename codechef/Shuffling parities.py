import random
import itertools
for _ in range(int(input())):
    n = int(input())
    b = list(itertools.permutations(list(map(int,input().split()))))
    s = 0
    for i in b:
        count=0
        for j in range(n):
            count+=(i[j]+j+1)%2
        if count>s:
            s = count
    print(s)
               