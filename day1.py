import re

# get the input
with open("day1_input.txt") as f:
    data = f.readlines()

# part 1
# read every line, get the first and last number, store
def get_nums(data: list) -> list:
    nums = []
    tmp = ""

    for line in data:
        for char in line:
            if char.isnumeric():
                tmp = tmp + char
                break

        for char in reversed(line):
            if char.isnumeric():
                tmp = tmp + char
                break

        nums.append(int(tmp))
        tmp = ""

    return nums

# part 2
# turn string digits into numeric digits
# be careful with overlapping numbers (e.g. 'twone'), brute force if you have to
# edit: I had to
def make_numeric(data: list) -> list:
    numeric = {"oneight": "18", "twone": "21", "threeight": "38", "fiveight": "58", "eightwo": "82", "nineight": "98",
               "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
               "six": "6", "seven": "7","eight": "8", "nine": "9"}

    stringnums = re.compile(r"|".join(re.escape(key) for key in numeric.keys()))
    new_data = []

    for line in data:
        new_line = stringnums.sub(lambda x: numeric[x.group()], line)
        new_data.append(new_line)

    return new_data

# add all the things
def solve(thing: list):
    solution1 = sum(get_nums(thing))
    solution2 = sum(get_nums(make_numeric(thing)))

    print(f"part 1: {solution1}, part 2: {solution2}")

# do the thing
solve(data)