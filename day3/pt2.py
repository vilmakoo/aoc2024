import re

with open("./input") as f:
    memory = f.read()

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

mul_on = True

sum = 0

splitted = re.split(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", memory)
for s in splitted:
    s = s.strip()
    # if not s:
    #     continue

    if re.fullmatch(do_pattern, s):
        mul_on = True
    elif re.fullmatch(dont_pattern, s):
        mul_on = False
    elif re.fullmatch(mul_pattern, s):
        if mul_on:
            match = re.match(mul_pattern, s)
            x = int(match.group(1))
            y = int(match.group(2))
            sum += x*y

print(sum)