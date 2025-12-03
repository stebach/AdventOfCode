"""
Solution for day 03 of year 2025
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = tuple(int(x) for x in line.strip())
    return line

def highest_voltage(data, number_of_batteries):
    result = 0
    for line in data:
        batteries = []
        pos = 0
        while len(batteries) < number_of_batteries:
            lastpos = -number_of_batteries + len(batteries) +1
            maxnum = max(line[pos:lastpos if lastpos !=0 else None])
            batteries.append(maxnum)
            pos = line[pos:].index(maxnum) +1+pos
        
        result += int("".join(str(x) for x in batteries))
    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = highest_voltage(data, 2)

    # Part 2
    solution2 = highest_voltage(data, 12)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
