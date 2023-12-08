"""
Solution for day 07 of year 2018
"""

import os
from functools import reduce

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(tuple(map(lambda line: line.strip(), inputdata.readlines())))

def parse_lines(lines):
    retVal = {}
    for line in lines:
        if not line[36:37] in retVal:
            retVal[line[36:37]] = []
        if not line[5:6] in retVal:
            retVal[line[5:6]] = []
        retVal[line[36:37]].append(line[5:6])
    return retVal

def part1(data):
    """Solve part 1"""
    result = ""
    sorted_keys = sorted(list(data.keys()))
    while (len(result) < len(data)):
        for check in [x for x in sorted_keys if x not in result]:
            available = True
            for check2 in data[check]:
                if not check2 in result:
                    available = False
                    break;
            if available:
                result = result + check
                break;
    return result

def part2(data, worker_count=5, fixed_seconds=60):
    """Solve part 2"""
    result = ""
    workers = {}
    sorted_keys = sorted(list(data.keys()))
    time = 0
    while (len(result) < len(data)):
        if len(workers) < worker_count:
            for check in [x for x in sorted_keys if x not in result and x not in workers]:
                available = True
                for check2 in data[check]:
                    if not check2 in result:
                        available = False
                        break;
                if available:
                    workers[check] = ord(check) - 64  + fixed_seconds
                    if len(workers) == worker_count:
                        break;
        time = time + 1

        workers = {k: v -1 if v > 0 else 0 for k, v in workers.items()}
        finished = [k for k, v in workers.items() if v < 1]

        for char in finished:
            del workers[char]
            result = result + char

    return time

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
