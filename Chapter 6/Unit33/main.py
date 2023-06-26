def is_valid_move(maze, row, col, N):
    return row >= 0 and col >= 0 and row < N and col < N and maze[row][col] == 1


def maze_route(maze, N):
    solution = [[0] * N for _ in range(N)]
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    if not dfs_helper(maze, 0, 0, solution, N, directions):
        print("No escape route found.")
        return False
    print("Escape route:")
    for row in solution:
        print(row)
    return True


def dfs_helper(maze, row, col, solution, N, directions):
    if row == N - 1 and col == N - 1:
        solution[row][col] = 1
        return True
    if is_valid_move(maze, row, col, N):
        solution[row][col] = 1
        for direction in directions:
            next_row = row + direction[0]
            next_col = col + direction[1]
            if dfs_helper(maze, next_row, next_col, solution, N, directions):
                return True
        solution[row][col] = 0
        return False

    return False


N = 4

maze = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [0, 0, 0, 0]
]

maze_route(maze, N)
