n= [list(map(int,input().split())) for i in range(6)]
s=[]
for i in range(4):
    for j in range(4):
        s.append(n[i][j]+n[i][j+1]+n[i][j+2]+n[i+1][j+1]+n[i+2][j]+n[i+2][j+1]+n[i+2][j+2])
print(max(s))