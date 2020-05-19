import sys
n,c=int(input()),[int(x) for x in input().split()]
count=0
i=0
while i<len(c):
    count=-1
    i=0
    while i<len(c):
        count +=1
        if i<len(c)-2 and c[i+2]==0:
            i += 1
        i += 1 
print(count)