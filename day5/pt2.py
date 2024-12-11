with open("./input") as f:
    input = f.read().split("\n\n")

rules = list(map(lambda x: (int(x.split("|")[0]), int(x.split("|")[1])), input[0].split("\n")))
updates = input[1].split("\n")

not_in_order = []

for u in updates:
    pages = list(map(int, u.split(",")))
    original_pages = pages[:]
    reordered = False

    while True:
        modified = False
        for first, second in rules:
            if first in pages and second in pages:
                if pages.index(first) > pages.index(second):
                    pages.remove(first)
                    pages.insert(pages.index(second), first)
                    modified = True
        if not modified:
            break
    
    if pages != original_pages:
        not_in_order.append(pages)

total_middle_sum = 0
for u in not_in_order:
    total_middle_sum += u[len(u)//2]

print(total_middle_sum)