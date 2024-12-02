input = list(open("./input"))

left = []
right = []

for line in input:
    locs = line.split()
    left.append(int(locs[0]))
    right.append(int(locs[1]))

left.sort()
right.sort()

sum = 0
for i in range(len(left)):
    sum += abs(left[i] - right[i])

print(sum)