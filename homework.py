import random
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)

for i in range (3):
    for j in range (3):
        print(matrix[i][j], end=" ")
    print("\n")

rows=int(input("How many rows?:"))
columns=int(input("How many columns"))

matrix1 = []

for i in range(rows):
    temp = []
    for i in range(columns):
        n = int(input("What numbers do you want?:"))
        temp.append(n)
    matrix1.append(temp)
for i in range(rows):
    for j in range(columns):
        print(matrix1[i][j], end=" ")
    print("\n")

matrixA = [[13,8],[12,10]]
matrixB = [[5,2],[4,1]]
result = [[0,0],[0,0]]
2

print("Matrix Subtraction:")

for i in range(0,2):
    for j in range(0,2):
        result[i][j] = matrixA[i][j] - matrixB[i][j]
for i in range(0,2):
    for j in range(0,2):
        print(result[i][j], end= " ")
    print("\n")

