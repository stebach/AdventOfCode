"""
Solution for day 14 of year 2018
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return int(inputdata.read())

def make_recipes(data, runs):
    pos1 = 0
    pos2 = 1
    while len(data) < runs + 10:
        quality = str(data[pos1] + data[pos2])
        for char in quality:
            data.append(int(char))
        pos1 = (pos1 + data[pos1] + 1) % len(data)
        pos2 = (pos2 + data[pos2] + 1) % len(data)
    return int("".join([str(x) for x in data[runs:runs+10]]))

def part1(data):
    """Solve part 1"""
    return make_recipes([3,7], data)

def search_in_recipes(pattern, data):
    pos1 = 0
    pos2 = 1
    result = "".join([chr(x) for x in data])
    while pattern not in  result:
        quality = str(data[pos1] + data[pos2])
        for char in quality:
            data.append(int(char))
            result = result[-len(pattern):] + char
        pos1 = (pos1 + data[pos1] + 1) % len(data)
        pos2 = (pos2 + data[pos2] + 1) % len(data)
    return "".join([str(x) for x in data]).index(pattern)

def part2(data):
    """Solve part 2"""
    print(search_in_recipes(str(data), [3,7]))
    exit()
    return data

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
