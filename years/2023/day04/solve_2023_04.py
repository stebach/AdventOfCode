"""
Solution for day 04 of year 2023
"""

import os
import regex

def parse_line(line):
    result = regex.match(r'^Card[ ]+([0-9]+): ([0-9, ]+)\|([0-9, ]+)', line)
    return [
        int(result.group(1)),
        list(map(int, [x for x in result.group(2).strip().split(" ") if x != ""])),
        list(map(int, [x for x in result.group(3).strip().split(" ") if x != ""]))
    ];

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def part1(data):
    """Solve part 1"""
    return sum(map(lambda x: 2 ** (len(set(x[1]) & set(x[2]))-1) if len(set(x[1]) & set(x[2])) > 0 else 0, data))

def part2(data):
    """Solve part 2"""
    cardcounts = [1] * len(data)
    for card in data:
        matches = len(set(card[1]) & set(card[2]))
        for x in range(card[0], min(card[0] + matches, len(data))):
            cardcounts[x] = cardcounts[x] + cardcounts[card[0] - 1]
    return sum(cardcounts)

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
