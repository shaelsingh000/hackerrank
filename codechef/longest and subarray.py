from math import log
for _ in range(int(input())):
    n = int(input())
    if n==1:
        print(1)
    else:
        a = int(log(n,2)) 
        x=(2**(a-1))
        y = (2**(a+1))
        z = 2**a
        if n == z:
            print(n-x)
        elif n<y:
            print(max(((n-z)+1),(z-x)))