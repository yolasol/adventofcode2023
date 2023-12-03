# part 1
import re

# get the input
with open("day2_input.txt") as f:
    data = f.readlines()

# maybe clean this up a little to do the processing in one function and the solving in another

# functions are cool
def solve1(thing, red: int, blue: int, green: int) -> int:
    pattern = re.compile(r"\d+\s+\w+")
    amount = re.compile(r"\d+")
    gamenumber = 0
    solution = 0

    for game in thing:
        gamenumber += 1
        flag = 0

        draws = game.split(";")
        for draw in draws:
            reds = blues = greens = 0
            cubes = pattern.findall(draw)

            for cube in cubes:
                r = amount.findall(cube)
                if "red" in cube:
                    reds += int(r[0])
                if "blue" in cube:
                    blues += int(r[0])
                if "green" in cube:
                    greens += int(r[0])

            if reds > red or blues > blue or greens > green:
                flag += 1

        if flag == 0:
            solution += gamenumber

    return solution

# I am an idiot who cannot read
# part 2
def solve2(thing, red, blue, green):
    pattern = re.compile(r"\d+\s+\w+")
    amount = re.compile(r"\d+")
    gamenumber = 0
    solution = 0

    for game in thing:
        gamenumber += 1
        draws = game.split(";")
        reds = blues = greens = 0

        for draw in draws:
            cubes = pattern.findall(draw)
            for cube in cubes:
                r = amount.findall(cube)

                if "red" in cube:
                    if int(r[0]) > reds:
                        reds = int(r[0])
                if "blue" in cube:
                    if int(r[0]) > blues:
                        blues = int(r[0])
                if "green" in cube:
                    if int(r[0]) > greens:
                        greens = int(r[0])

        print(f"minimum reds: {reds}, minimum blues: {blues}, minimum greens: {greens}")

        cubed = reds * greens * blues
        solution += cubed

    return solution

# solve all the things
# print(solve1(data, 12, 14, 13))
print(solve2(data, 12, 14, 13))