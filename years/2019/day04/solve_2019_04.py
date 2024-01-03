"""
Solution for day 04 of year 2019
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple([int(x) for x in inputdata.read().strip().split('-')])

def check_password(password, part2=False):
    numbers = [int(x) for x in str(password)]
    double_found = False
    for x in range(len(numbers) - 1):
        if numbers[x] > numbers[x+1]:
            return False
        elif numbers[x] == numbers[x+1]:
            if part2:
                if (x == 0 or numbers[x-1] != numbers[x]) and (x == len(numbers) - 2 or numbers[x+2] != numbers[x]):
                    double_found = True
            else:
                double_found = True
    return double_found

def part1(data):
    """Solve part 1"""
    count = 0
    for x in range(data[0], data[1] + 1):
        if check_password(x):
            count += 1
    return count

def part2(data):
    """Solve part 2"""
    count = 0
    for x in range(data[0], data[1] + 1):
        if check_password(x, True):
            count += 1
    return count


def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
