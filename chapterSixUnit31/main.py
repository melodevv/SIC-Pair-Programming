# ===================================================
#                  QUESTION ONE
# ===================================================

def find_minimum(row, col, triangle):
    if row == len(triangle):
        return 0
    else:
        minimum = min(find_minimum(row + 1, col, triangle), find_minimum(row + 1, col + 1, triangle))
        return triangle[row][col] + minimum


triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
minimum = find_minimum(0, 0, triangle)
print("The minimum cost is ", minimum)

