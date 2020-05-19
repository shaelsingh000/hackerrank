import sys
def minimumBribes(Q):
    moves = 0 
    Q = [P-1 for P in Q]
    for i,P in enumerate(Q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                moves += 1
    print(moves)
if __name__ == '__main__':
    n=int(input())
    b=[]
    l=[]
    for i in range(n):
        a=[]
        l.append(int(input()))
        a=[int(x) for x in input().split()]
        b.append(a)
    for i in b:
        minimumBribes(i)