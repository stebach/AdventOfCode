"""
Solution for day 01 of year 2022
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        data = inputdata.read()
        return parse_data(data)

def parse_data(data):
        data = data.split("\n\n")
        data = [tuple(map(int, row.split("\n"))) for row in data]
        data.sort(key=sum, reverse=True)
        return data

def part1(data):
    """Solve part 1"""
    return sum(data[0])

def part2(data):
    """Solve part 2"""
    return sum(map(sum, data[0:3]))

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
