def count_clusters(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
 
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            grid[r][c] == 0 or (r, c) in visited):
            return
 
        visited.add((r, c))
 
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
 
    count = 0
 
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and (i, j) not in visited:
                dfs(i, j)
                count += 1
 
    return count
 
 
grid = [
    [1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 1, 0, 0]
]
 
print(count_clusters(grid))