matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
a = "false"
for i in range(len(matrix)):
    if matrix[i][0]>target:
        break
    elif target in matrix[i]:
        a = "true"
        break
print(a)
            