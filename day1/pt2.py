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
for kis in left:
    # import pdb; pdb.set_trace()
    times = 0
    for koi in right:
        if kis == koi:
            times += 1
    sum += kis * times


print(sum)