import itertools
import re
from collections import defaultdict

# get the input
# note to self: readlines() gives an answer that's too high
with open("day3_input.txt") as f:
    data = f.read().strip().split("\n")

# part 1
# itertools.product() finds all possible combinations of two arrays
# this creates all coordinates in a 9x9 grid
adjacent_coordinates = list(itertools.product((-1, 0, 1), (-1, 0, 1)))

# get coordinates of the symbols in the engine schematic
symbols = {
    (a, b)
    for a, row in enumerate(data)
    for b, char in enumerate(row)
    if char != "." and not char.isdigit()
    }

solution = 0
# part 2
solution2 = 0
gears = defaultdict(list)

# find the numbers and their coordinates
for x, y in enumerate(data):
    for match in re.finditer(r"\d+", y):
        number = int(match.group(0))
        # now get the coordinates and see if they are adjacent to a symbol
        adjacent = {
            (x + a, j + b)
            for a, b in adjacent_coordinates
            for j in range(match.start(), match.end())
            }
        # if a symbol coordinate matches the coordinates adjacent to a number, the number is a part number
        if symbols & adjacent:
            solution += number
        # part 2: is mayonnaise a gear?
        for symbol in symbols & adjacent:
            gears[symbol].append(number)

# part 2
for thing in gears.values():
    if len(thing) == 2:
        solution2 += thing[0] * thing[1]

# solve all the things
print(solution)
print(solution2)
