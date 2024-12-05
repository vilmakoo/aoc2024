import re

with open("./input") as f:
    memory = f.read()

multiplications = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)

sum = 0
for mul in multiplications:
    x = int(mul[0])
    y = int(mul[1])
    sum += x*y

print(sum)