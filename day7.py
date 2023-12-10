# get the input
with open("day7_input.txt") as f:
    data = f.readlines()

# functions are cool
# part 1
def kind_of_hand(hand: str):
    types = [
            [5],            # five of a kind (0)
            [4, 1],         # four of a kind (1)
            [3, 2],         # full house (2)
            [3, 1, 1],      # three of a kind (3)
            [2, 2, 1],      # two pair (4)
            [2, 1, 1, 1],   # one pair (5)
            [1, 1, 1, 1, 1] # high card (6)
            ]
    # list comprehension is cool too
    # turn every hand into a hand type regardless of value
    # this is going to come back to bite me in part 2 isn't it
    counts = [hand.count(card) for card in set(hand)]
    counts.sort(reverse=True)

    return types.index(counts)

# part 2
def kind_of_hand_2(hand: str):
    types = [
        [5],  # five of a kind (0)
        [4, 1],  # four of a kind (1)
        [3, 2],  # full house (2)
        [3, 1, 1],  # three of a kind (3)
        [2, 2, 1],  # two pair (4)
        [2, 1, 1, 1],  # one pair (5)
        [1, 1, 1, 1, 1]  # high card (6)
    ]

    # ignore jokers
    counts = [hand.count(card) for card in set(hand) if card != "J"] or [0]
    counts.sort(reverse=True)
    # add jokers to the highest option
    counts[0] += hand.count("J")

    return types.index(counts)

# turn each hand into its card value for comparison
def card_value(hand: str, part: int):
    if part == 1:
        values = 'AKQJT98765432'
    elif part == 2:
        values = 'AKQT98765432J'
    return (values.index(card) for card in hand)

# split each hand
def sort_hands(thing: list, part: int) -> list:
    hands = []
    for line in data:
        hand, bid = line.split()
        if part == 1:
            h = (
                kind_of_hand(hand),
                # * is cool and will unpack values from iterable objects
                *card_value(hand, part),
                int(bid)
                )
            hands.append(h)
        if part == 2:
            h = (
                kind_of_hand_2(hand),
                *card_value(hand, part),
                int(bid)
                )
            hands.append(h)

    return hands

# solve all the things
def solve(thing: list, part: int) -> int:
    if part == 1:
        hands = sort_hands(thing, 1)
    elif part == 2:
        hands = sort_hands(thing, 2)

    hands.sort(reverse=True)
    winnings = 0

    for rank, hand in enumerate(hands):
        # rank * bid
        winnings += ((rank+1) * hand[-1])

    return winnings

print(solve(data, 2))