# ===================================================
#                  QUESTION ONE
# ===================================================


def tromino(board, size, missing_row, missing_col, row_start, col_start):
    if size == 2:
        tile_count = 1
        for i in range(2):
            for j in range(2):
                if board[row_start + i][col_start + j] == 0:
                    board[row_start + i][col_start + j] = tile_count
                tile_count += 1
        return
    quad_row = missing_row >= row_start + size // 2
    quad_col = missing_col >= col_start + size // 2
    middle_col = col_start + size // 2
    middle_row = row_start + size // 2
    tromino_count = 1
    for i in range(2):
        for j in range(2):
            if quad_row == i and quad_col == j:
                continue
            board[middle_row + i][middle_col + j] = tromino_count
            tromino_count += 1

    tromino(board, size // 2, missing_row, missing_col, row_start, col_start + size // 2)
    tromino(board, size // 2, middle_row - 1, middle_col, row_start, col_start)
    tromino(board, size // 2, middle_row, middle_col - 1, row_start + size // 2, col_start)
    tromino(board, size // 2, middle_row, middle_col, row_start + size // 2, col_start + size // 2)


def new_tromino(n, missing_row, missing_col):
    board = [[0] * n for _ in range(n)]
    tromino(board, n, missing_row, missing_col, 0, 0)
    for row in board:
        print(row)


n = 4
row = 2
col = 1

new_tromino(n, row, col)
