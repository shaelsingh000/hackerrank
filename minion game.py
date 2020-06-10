def minion_game(string):
    c1,c2=0,0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            c2+=len(s)-i
        else:
            c1+=len(s)-i
    if c1>c2:
        print("Stuart",c1)
    elif c1<c2:
        print("Kevin",c2)
    elif c1==c2:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)