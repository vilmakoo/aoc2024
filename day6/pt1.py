# got frustrated and used a lot of chatgpt to help with this one. my ugly code is in `pt1_oma.py`

with open("./input") as f:
    input = f.read()
    mp = [list(line) for line in input.split("\n")]  # map

x_limit = len(mp[0]) - 1
y_limit = len(mp) - 1

def find_start():
    for y in range(len(mp)):
        for x in range(len(mp[y])):
            if mp[y][x] == "^":
                return y, x

directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

def move():
    visited = set()

    y, x = find_start()
    direction = "^"
    
    while True:
        visited.add((x, y))
        
        dx, dy = directions[direction]
        new_x, new_y = x + dx, y + dy
        
        if 0 <= new_x <= x_limit and 0 <= new_y <= y_limit:
            if mp[new_y][new_x] == "#":
                direction = turns[direction]
            else:
                x, y = new_x, new_y
        else:
            break

    return len(visited)

visited_count = move()

print(visited_count)
