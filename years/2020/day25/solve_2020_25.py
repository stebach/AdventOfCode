"""
Solution for day 25 of year 2020
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

def get_loopsizes(data):
    result = []
    num = 1
    count = 0
    while len(result) < 2:
        count += 1
        num = run_loop(num, 7, 1)
        if num in data:
            result.append(count)
    return result

def run_loop(number, subjectnumber, loopsize):
    result = number
    for x in range(loopsize):
        result *= subjectnumber
        result = result % 20201227
    return result

def get_encryption_key(data):
    loopsizes = get_loopsizes(data)
    num = run_loop(1, 7, loopsizes[0])
    return run_loop(1, num, loopsizes[1])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_encryption_key(data)

    return solution1, None

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
