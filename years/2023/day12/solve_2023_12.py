"""
Solution for day 12 of year 2023
"""

import os
import regex
from functools import lru_cache

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    input, input2 = line.strip().split(' ')
    return [input, tuple(map(int, input2.split(',')))]

@lru_cache
def count_arrangements(records1, records2):

    if not '#' in records1 and not '?' in records1:
        if len(records2) > 0:
            return 0
        return 1

    if len(records2) == 0:
        if '#' in records1:
            return 0
        return 1

    if sum(records2) > records1.count('#') + records1.count('?'):
        return 0

    records1 = regex.sub('^\.+','',records1)

    count = 0
    next_record = records2[0]
    rest = records2[1:]

    for x in range(len(records1) - sum(records2) + len(records2)-1):
        if not '#' in records1[:x] and not '.' in records1[x:x + next_record] and not '#' in records1[x + next_record]:
            add_count = count_arrangements(records1[x + next_record+1:],rest)
            count = count + add_count

    return count

def part1(data):
    """Solve part 1"""
    return sum([count_arrangements('.' + x[0] + '.', x[1]) for x in data])

def unfold(data):
    newstring = '?'.join([data[0]] * 5)
    return [newstring, data[1] * 5]

def part2(data):
    """Solve part 2"""
    unfolded = list(map(unfold, data))
    return sum(list(map(lambda x: count_arrangements('.' + x[0] + '.', x[1]), unfolded)))

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
