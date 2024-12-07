def find_next_letter(coords, letter, direction):
    xmas = ["X", "M", "A", "S"]

    if letter == 4:
        return 1  # XMAS has been found
    
    i, j = coords
    n, m = len(input), len(input[0])

    if direction == "down":       # Move down
        ni, nj = i + 1, j
    elif direction == "up":       # Move up
        ni, nj = i - 1, j
    elif direction == "left":     # Move left
        ni, nj = i, j - 1
    elif direction == "right":    # Move right
        ni, nj = i, j + 1
    elif direction == "dl":       # Down-left
        ni, nj = i + 1, j - 1
    elif direction == "dr":       # Down-right
        ni, nj = i + 1, j + 1
    elif direction == "ul":       # Up-left
        ni, nj = i - 1, j - 1
    elif direction == "ur":       # Up-right
        ni, nj = i - 1, j + 1
    else:
        return 0  # Invalid direction

    if 0 <= ni < n and 0 <= nj < m and input[ni][nj] == xmas[letter]:
        return find_next_letter((ni, nj), letter + 1, direction)
    else:
        return 0
    

def find_xmax():
    sum = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "X":
                sum += find_next_letter((i, j), 1, "down")
                sum += find_next_letter((i, j), 1, "up")
                sum += find_next_letter((i, j), 1, "left")
                sum += find_next_letter((i, j), 1, "right")
                sum += find_next_letter((i, j), 1, "dl")  # down left
                sum += find_next_letter((i, j), 1, "dr")  # down right
                sum += find_next_letter((i, j), 1, "ul")  # up left
                sum += find_next_letter((i, j), 1, "ur")  # up right
    return(sum)

input = list(open("./input"))
input = [list(s.strip()) for s in input]  # convert to a 2d array of characters

sum = find_xmax()

print(sum)