"""
Solution for day 07 of year 2023
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def translate_card_val(card, with_jokers = False):
    if card.isnumeric():
        return int(card)
    if card == 'T':
        return 10
    elif card == 'J':
        if with_jokers:
            return 0
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == 'A':
        return 14
    else:
        return 0

def calc_hand_value(hand, with_jokers=False):
    type = 0
    hand_to_use = hand
    card_count = 5
    if with_jokers:
        hand_to_use = [x for x in hand if x != 0]
        card_count = len(hand_to_use)

    different_cards = list(set(hand_to_use))
    different_cards_count = len(different_cards)

    if different_cards_count == 1: #five of a kind
        type = 7
    elif different_cards_count == 2: #four of a kind or full house
        if (card_count == 4 and hand.count(different_cards[0]) != 2) or card_count < 4:
            type = 6 #promote to four of a kind
        elif hand.count(different_cards[0]) == 1 or hand.count(different_cards[0]) == 4:
            type = 6 #four of a kind
        else:
            type = 5 #full house
    elif different_cards_count == 3: #three of a kind or two pair
        if card_count < 5:
            type = 4 #promote to three of a kind
        elif hand.count(different_cards[0]) == 2 or hand.count(different_cards[1]) == 2:
            type = 3 #two pair
        else:
            type = 4 #three of a kind
    elif different_cards_count == 4: #one pair
        type = 2
    else: #high card
        if card_count == 0:
            type = 7 # promote to five of a kind
        else:
            type = 1

    return type * 10000000000 + hand[0] * 100000000 + hand[1] * 1000000 + hand[2] * 10000 + hand[3] * 100 + hand[4]

def parse_line(line):
    line = line.strip().split(' ')
    values = [translate_card_val(x) for x in [*line[0]]]
    values2 = [translate_card_val(x, True) for x in [*line[0]]]
    return [line[0], int(line[1]), values, calc_hand_value(values), values2, calc_hand_value(values2, True)]

def part1(data):
    """Solve part 1"""
    return sum([(idx + 1) * x[1] for idx,x in enumerate(sorted(data, key=lambda x: x[3]))])

def part2(data):
    """Solve part 2"""
    return sum([(idx + 1) * x[1] for idx,x in enumerate(sorted(data, key=lambda x: x[5]))])

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
