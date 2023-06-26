n = int(input("Enter n: "))


matrix = [[0] * n for _ in range(n)]
num = 1
direction = 1
row = 0
col = 0
for i in range(n * n):
    matrix[row][col] = num
    if direction == 1:  
        col += 1
        if col == n or matrix[row][col] != 0:
            direction = -1
            col -= 1
            row += 1
    else:  
        col -= 1
        if col == -1 or matrix[row][col] != 0:
            direction = 1
            col += 1
            row += 1

    num += 1


for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(matrix[i][j], end=" ")
        else:
            print(f"({matrix[i][j]})", end=" ")
    print()