from collections import Counter
for _ in range(int(input())):
    n = input()
    s = Counter(list(input()))
    if s['0']<=0:
        print("0")
    elif s['1']<=0:
        print("0")
    else:
        if s['0']<s['1']:
            print(s['0']-1)
        else:
            print(s['1']-1)