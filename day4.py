# get the input
with open("day4_input.txt") as f:
    data = f.readlines()

# part 1
solution = 0

for line in data:
    points = 0
    x = 0
    # split cards
    line = line.split(":")
    line = line[1].split("|")

    # split winning numbers and numbers on scratchcard
    winning = [int(num) for num in line[0].split()]
    scratchcard = [int(num) for num in line[1].split()]

    # find winning numbers
    for num in scratchcard:
        if num in winning:
            x += 1
            if x == 1:
                points = 1
            elif x >= 1:
                points = points * 2

    solution += points

print(solution)

# part 2
# functions are cool
def solve(thing: list) -> int:
    # make a list of how many cards you have for each cardnumber
    cards = [0] * (len(thing) + 1)

    for line in thing:
        winning_nums = 0

        # split cards and get cardnumber
        line = line.split(":")
        cardnumber = int(line[0].split()[-1])

        # increase amount of this card by one
        cards[cardnumber] += 1

        # split winning numbers and numbers on scratchcard
        line = line[1].split("|")
        winning = [int(num) for num in line[0].split()]
        scratchcard = [int(num) for num in line[1].split()]

        # find winning numbers
        for num in scratchcard:
            if num in winning:
                winning_nums += 1

        # range from current card to new cards
        # for reasons unknown I get a leading zero, ignore for now because I am slow brained and it's 0 anyway
        for i in range(cardnumber + 1, cardnumber + winning_nums + 1):
            cards[i] += 1 * cards[cardnumber]

    return sum(cards)

print(solve(data))

