s = "Let's take LeetCode contest"
s=s.split()
b = ""
for i in s:
    b+=" "
    b+=i[-1::-1]
s = b.strip()
print(s)
