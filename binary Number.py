import re
print(len(max(re.compile("(1+)*").findall(bin(int(input()))))))