import sys
def minswap(a):
    c=0
    for pos,val in enumerate(a,1):
        if pos==val:
            pass
        else:
            k=a.index(pos)
            l=a[pos-1]
            a[pos-1]=pos
            a[k]=l
            c+=1
    print(c)
if __name__ == "__main__":
    n=int(input())
    a=[int(x) for x in input().split()]
    minswap(a)