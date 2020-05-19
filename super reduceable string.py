def super_reduced_string(s):
    r = []
    for c in s:
        last = r.pop() if r else ""
        if c != last: r.extend([last, c])
    return "".join(r) or "Empty String"
if __name__ == "__main__":
    s=input()
    print(super_reduced_string(s))