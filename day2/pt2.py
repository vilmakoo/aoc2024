input = list(open("./input"))

sum = 0

for line in input:
    levels = list(map(int, line.split()))
    # print(levels)

    def check_safeness(li, bad_level_removed):
        increasing = False
        if li[1] > li[0]:
            increasing = True

        for i in range(len(li) - 1):
            if ((increasing and li[i+1] < li[i]) or 
            (not increasing and li[i+1] > li[i]) or
            (abs(li[i+1] - li[i]) < 1) or
            (abs(li[i+1] - li[i]) > 3)):
                if bad_level_removed is False:
                    first = li.copy()
                    first.pop(i)
                    second = li.copy()
                    second.pop(i+1)
                    safe = check_safeness(first, True) or check_safeness(second, True)
                    if not safe and i > 0:
                        third = li.copy()
                        third.pop(i-1)
                        return check_safeness(third, True)
                    return safe
                else:
                    return False
        return True
    
    safe = check_safeness(levels, False)
    if safe:
        sum += 1

print(sum)
            