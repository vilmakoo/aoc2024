with open("./test_input") as f:
    input = f.read()
    mp = [list(line) for line in input.split("\n")]  # map

x_limit = len(mp[0]) - 1
y_limit = len(mp) - 1

def find_start():
    for y in range(len(mp)):
        for x in range(len(mp[y])):
            if mp[y][x] == "^":
                return y, x

def move(dr, x, y):
    positions = 0  # maybe use a list of visited?

    if dr == "^":
        if y == 0:
            return positions  # leaving area
        elif mp[y-1][x] == "#":
            positions += 1
            return positions + move(">", x+1, y)
        else:
            positions += 1
            return positions + move(dr, x, y-1)
    elif dr == ">":
        if x == x_limit:
            return positions
        elif mp[y][x+1] == "#":
            positions += 1
            return positions + move("v", x, y+1)
        else:
            positions += 1
            return positions + move(dr, x+1, y)
    elif dr == "v":
        if y == y_limit:
            return positions
        elif mp[y+1][x] == "#":
            positions += 1
            return positions + move("<", x-1, y)
        else:
            positions += 1
            return positions + move(dr, x, y+1)
    elif dr == "<":
        if x == 0:
            return positions
        elif mp[y][x-1] == "#":
            positions += 1
            return positions + move("^", x, y-1)
        else:
            positions += 1
            return positions + move(dr, x-1, y)

start = find_start()
positions = move("^", start[1], start[0])

print(positions)