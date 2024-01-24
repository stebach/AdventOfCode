"""
Solution for day 09 of year 2020
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

def find_first_invalid(data, length):
    check = []
    for i in range(length):
        for j in range(length):
            if i != j:
                check.append(data[i] + data[j])
    for i in range(length, len(data)):
        if data[i] not in check:
            return data[i]
        else:
            for j in range(length - 1):
                check.pop(0)
                check.append(data[i] + data[i - 1 - j])

def find_continous(data, number):
    for i in range(len(data)):
        for j in range(len(data) - i):
            check = sum(data[i:j])
            if check > number:
                break
            if check == number:
                return data[i:j]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_first_invalid(data, 25)

    # Part 2
    continous = find_continous(data, solution1)
    solution2 = min(continous) + max(continous)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

