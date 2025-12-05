"""
Solution for day 05 of year 2025
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {
        'ranges': [],
        'ingredients': []
    }
    is_ingredients = False
    for x in lines:
        if is_ingredients:
            x = x.strip()
            if x == '':
                continue
            result['ingredients'].append(int(x))
            continue
        else:
            if x.strip() == '':
                is_ingredients = True
                continue
            result['ranges'].append(tuple(map(int, x.strip().split('-'))))
    return result

def part1(data):
    fresh_ingredients = 0
    for ingredient in data['ingredients']:
        for r in data['ranges']:
            if r[0] <= ingredient <= r[1]:
                fresh_ingredients += 1
                break
    return fresh_ingredients

def part2(data):
    ranges = []
    for r in sorted(data['ranges']):
        if not ranges or ranges[-1][1] < r[0]:
            ranges.append(r)
        else:
            ranges[-1] = (ranges[-1][0], max(ranges[-1][1], r[1]))
    result = 0
    for r in ranges:
        result += r[1] - r[0] + 1
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
