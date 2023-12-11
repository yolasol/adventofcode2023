import re
import numpy

# get the input
with open("day6_input.txt") as f:
    data = f.readlines()

# functions are cool
def parse(input: list, part: int) -> list:
    numbers = re.compile(r"(\d+)")
    if part == 1:
        t = numbers.findall(input[0])
        d = numbers.findall(input[1])

    elif part == 2:
        t = d = ""
        for char in input[0]:
            if char.isdigit():
                t += char
        for char in input[1]:
            if char.isdigit():
                d += char

    return t, d

def race(input: list, part: int) ->  int:
    time, distance = parse(input, part)
    solution = []

    if part == 1:
        for t, d in zip(time, distance):
            wins = 0
            # holding the button for either 0 second or the full time will never work
            for s in range(int(t)-1):
                result = (s + 1) * (int(t) - (s + 1))
                if result > int(d):
                    wins += 1
            solution.append(wins)
            solved = numpy.prod(solution)
    # does it take long if I do it like this? yes
    # do I care? no
    elif part == 2:
        solved = 0
        for s in range(int(time) - 1):
            result = (s + 1) * (int(time) - (s + 1))
            if (result - 1) > int(distance):
                solved += 1

    return solved

# is mayonnaise a solution?
print(race(data, 2))

