def unique_paths(m, n):
    grid = []
    for i in range(m):
        grid.append([])
        for j in range(n):
            grid[i].append(1)
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = int(grid[i-1][j]) + int(grid[i][j-1])
    return grid[m-1][n-1]


print(unique_paths(3, 7))
