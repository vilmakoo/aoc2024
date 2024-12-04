input = list(open("./input"))

safe_count = 0

for line in input:
    levels = list(map(int, line.split()))
    print(levels)
    
    increasing = levels[1] > levels[0] if len(levels) > 1 else None

    safe = True

    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        if ((increasing and diff < 1) or
            (not increasing and diff > -1) or
            abs(diff) < 1 or
            abs(diff) > 3):
            safe = False
            break
    
    if safe:
        safe_count += 1

print(safe_count)
            
