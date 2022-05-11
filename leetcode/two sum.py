a = list(map(int,input().split()))
t = int(input())
hash_table = dict()

for i, num in enumerate(a):
    try:
        hash_table[t - num]
        print([hash_table[t - num]+1, i+1])
    except KeyError:
        hash_table[num] = i