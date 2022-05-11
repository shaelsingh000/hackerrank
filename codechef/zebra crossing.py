from collections import Counter
for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    a = Counter(s)
    if '0' not in s or '1' not in s:
        print(-1)
    else:
        if s[0] == '0':
            one = k//2 + k%2
            zero = k//2
            x = '0'
            y = '1'
        else:
            zero = k//2 + k%2
            one = k//2
            x = '1'
            y = '0'
        if a['1']<one or a['0']<zero:
            print(-1)
        elif k%2 == 0:
            print(s.rindex(x)+1)
        elif k%2 == 1:
            print(s.rindex(y)+1)