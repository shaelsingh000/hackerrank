import sys
def maxpali(s,n,k):
    c=0
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-1-i]:
            c+=1
    if c>k:
        return '-1'
    if k>len(s):
        return '9'*len(s)
    c=k-c
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-1-i] and c!=0:
            if s[i]!='9' and s[len(s)-1-i]=='9':
                c=c-1
            s[i]=s[len(s)-1-i]='9'
        elif s[i]!=s[len(s)-1-i] and c == 0:
            s[i] = s[len(s)-i-1] = max(s[i],s[len(s)-i-1])
        elif s[i]==s[len(s)-1-i] and c>1 and s[i]!='9':
            c -= 2
            s[i] = s[len(s)-1-i] = '9'
        else:
            continue
    if c>0 and len(s)%2==1:
        s[len(s)//2]='9'
    if s==s[::-1]:
        return ''.join(s)
if __name__ == "__main__":
    n,k=[int(x) for x in input().split()]
    s=list(input())
    o=maxpali(s,n,k)
    print(o)