from collections import Counter

def max_used(a,s):
    c = Counter(a)
    keymax = max(zip(c.values(), c.keys()))[1]
    return s[keymax]
    
s={
    "P":"Pediatrics",
    "O":"Orthopedics",
    "E":"ENT"
}
a = list(input().split(","))
print(max_used(a,s))