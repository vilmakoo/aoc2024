with open("./input") as f:
    input = f.read().split("\n\n")

rules = list(map(lambda x: (int(x.split("|")[0]), int(x.split("|")[1])), input[0].split("\n")))
updates = input[1].split("\n")

in_order = []

for u in updates:
    pages = list(map(int, u.split(",")))
    right_order = True
    for first, second in rules:
        if first in pages and second in pages:
            if pages.index(first) > pages.index(second):
                right_order = False
                break

    if right_order:
        in_order.append(u)

total_middle_sum = 0
for u in in_order:
    pages = list(map(int, u.split(",")))
    total_middle_sum += pages[int(len(pages)//2)]

print(total_middle_sum)