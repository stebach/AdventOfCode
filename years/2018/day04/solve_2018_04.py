"""
Solution for day 04 of year 2018
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    current_guard = 0
    current_day = ''
    asleep = 0
    guards = {}
    lines = sorted(lines)
    for line in lines:
        line = line.strip()
        result = regex.match(r'^\[([0-9]{4}-[0-9]{2}-[0-9]{2}) ([0-9]{2}):([0-9]{2})\] (Guard #([0-9]+) begins shift|falls asleep|wakes up)$', line)
        if result.group(4) == 'wakes up':
            for x in range(asleep, int(result.group(3))):
                guards[current_guard][x] = guards[current_guard][x] + 1
        elif result.group(4) == 'falls asleep':
            asleep = int(result.group(3))
        elif len(result.groups()) == 5:
            current_guard = int(result.group(5))
            if not current_guard in guards:
                guards[current_guard] = [0] * 61
    return guards

def part1(data):
    """Solve part 1"""
    sums = { k: sum(v) for k, v in data.items() }
    sortedSums = dict(sorted(sums.items(), key=lambda x: x[1], reverse=True))
    guard = list(sortedSums.keys())[0]

    return data[guard].index(max(data[guard])) * guard

def part2(data):
    """Solve part 2"""
    maxs = { k: max(v) for k, v in data.items() }
    sortedMaxs = dict(sorted(maxs.items(), key=lambda x: x[1], reverse=True))
    guard = list(sortedMaxs.keys())[0]

    return data[guard].index(max(data[guard])) * guard

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
