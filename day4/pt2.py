def find_xmas_patterns(grid):
    sum = 0
    n, m = len(grid), len(grid[0])

    mases = ["MAS", "SAM"]

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            for mas1 in mases:
                for mas2 in mases:
                    if (
                        i - 1 >= 0 and j - 1 >= 0 
                        and grid[i - 1][j - 1] == mas1[0] 
                        and grid[i][j] == mas1[1] 
                        and i + 1 < n 
                        and j + 1 < m 
                        and grid[i + 1][j + 1] == mas1[2]
                    ):
                        if (i - 1 >= 0 and j + 1 < m 
                            and grid[i - 1][j + 1] == mas2[0] 
                            and
                            grid[i][j] == mas2[1] 
                            and i + 1 < n 
                            and j - 1 >= 0 
                            and grid[i + 1][j - 1] == mas2[2]
                        ):
                            sum += 1

    return sum

grid = [list(line.strip()) for line in open("./input")]
result = find_xmas_patterns(grid)
print(result)
