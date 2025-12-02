"""
Solution for day 02 of year 2025
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(parse_line(inputdata.readlines()))


def parse_line(line):
    line = (tuple([int(y) for y in x.split('-')]) for x in line[0].strip().split(','))
    return line

def parse_lines(lines):
    return [x for x in lines]

def part1(data):
    result = 0
    for range_start, range_end in data:
        number = range_start

        while number <= range_end:
            numstr = str(number)
            numstrlen = len(numstr)
            if numstrlen % 2 == 1:
                numstr = str(pow(10, numstrlen))
                number = int(numstr[0:(numstrlen + 1)//2] + numstr[0:(numstrlen + 1)//2])
            else:
                if numstr[0:numstrlen//2] == numstr[numstrlen//2:numstrlen]:
                    result += number
                    number += 1 + pow(10, numstrlen//2)
                else:
                    if int(numstr[0:numstrlen//2]) > int(numstr[numstrlen//2:numstrlen]):
                        number = int(numstr[0:numstrlen//2] + numstr[0:numstrlen//2])
                    else:
                        part = str(int(numstr[0:(numstrlen)//2]) + 1)
                        number = int(part + part)

    return result

def part2(data):
    result = 0
    for range_start, range_end in data:
        for number in range(range_start, range_end + 1):
            is_invalid = False
            for partlen in range(1, len(str(number))//2 + 1):
                part = str(number)[0:partlen]
                numberlen = len(str(number))
                if numberlen % partlen == 0 and str(number) == part * (numberlen // partlen):
                    is_invalid = True
                    break
            if is_invalid:
                result += number
    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = part1(data)

    # Part 2
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
