"""
Solution for day 11 of year 2024
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return list(map(parse_line, inputdata.readlines()))[0]

def parse_line(line):
    return [int(x) for x in line.strip().split(' ')]

def number_of_stones(data, amount):
    cache = {}
    total = 0
    for stone in data:
        total += get_stone_result(stone, amount, cache)
    return total

def get_stone_result(stone, amount, cache):
    if amount == 0:
        return 1
    if stone not in cache:
        cache[stone] = {}
    if amount in cache[stone]:
        return cache[stone][amount]
    for i in range(1, amount + 1):
        if i not in cache[stone]:
            if stone == 0:
                cache[stone][i] = get_stone_result(1, i - 1, cache)
            elif len(str(stone)) % 2 == 0:
                strval = str(stone)
                cache[stone][i] = get_stone_result(int(strval[:len(strval)//2]), i - 1, cache) \
                     + get_stone_result(int(strval[len(strval)//2:]), i - 1, cache)
            else:
                cache[stone][i] = get_stone_result(stone * 2024, i - 1, cache)
    return cache[stone][amount]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = number_of_stones(data, 25)

    # Part 2
    solution2 = number_of_stones(data, 75)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
