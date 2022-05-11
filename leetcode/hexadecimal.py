n = 26
s = []
result = ''
hexa = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
while n > 0:
    s.append(n%16)
    n=n//16
s[:]=s[::-1]
print(s)
for i in s:
    result +=hexa[i]
print(result)