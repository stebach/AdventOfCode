"""
Solution for day 09 of year 2023
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return [int(x) for x in line.strip().split(' ')]

def predict(numbers, backwards=False):
    differences = [numbers[k + 1] - v for k,v in enumerate(numbers[:-1])]
    if sum(differences) == 0 and differences == [0] * len(differences):
        return numbers[0 if backwards else -1]
    if backwards:
        return numbers[0] - predict(differences, backwards)
    return predict(differences) + numbers[-1]

def predict_backwards(numbers):
    return predict(numbers, True)

def part1(data):
    """Solve part 1"""
    return sum(map(predict, data))

def part2(data):
    """Solve part 2"""
    return sum(map(predict_backwards, data))

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
