"""
Solution for day 22 of year 2020
"""

import os
from collections import deque
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    idx = 0
    retVal = (
        deque([]),
        deque([]),
    )
    for line in lines:
        line = line.strip()
        if line[0:7] == 'Player ':
            idx = int(line[7:-1]) - 1
        elif len(line) > 0:
            retVal[idx].append(int(line))
    return retVal

def play(data):
    while len(data[0]) > 0 and len(data[1]) > 0:
        card1 = data[0].popleft()
        card2 = data[1].popleft()
        if card1 > card2:
            data[0].append(card1)
            data[0].append(card2)
        else:
            data[1].append(card2)
            data[1].append(card1)

def play_recursive(data):
    prev = set()
    while len(data[0]) > 0 and len(data[1]) > 0:
        hash = ",".join([str(x) for x in data[0]])+"|"+",".join([str(x) for x in data[1]])
        if hash in prev:
            data[1].clear()
            return
        prev.add(hash)

        card1 = data[0].popleft()
        card2 = data[1].popleft()

        if len(data[0]) >= card1 and len(data[1]) >= card2:
            data2 = (
                deque(list(data[0])[0:card1]),
                deque(list(data[1])[0:card2]),
            )
            play_recursive(data2)
            if len(data2[0]) > 0:
                data[0].append(card1)
                data[0].append(card2)
            else:
                data[1].append(card2)
                data[1].append(card1)
        else:
            if card1 > card2:
                data[0].append(card1)
                data[0].append(card2)
            else:
                data[1].append(card2)
                data[1].append(card1)


def scoring(data):
    winner_cards = list(data[0]) if len(data[0]) > 0 else list(data[1])
    cards = len(winner_cards)
    return sum([x[1] * (cards - x[0]) for x in enumerate(winner_cards)])

def solve(data):
    """Solve the puzzle for the given input"""
    data2 = deepcopy(data)

    # Part 1
    play(data)
    solution1 = scoring(data)

    # Part 2
    play_recursive(data2)
    solution2 = scoring(data2)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
