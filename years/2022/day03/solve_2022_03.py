"""
Solution for day 03 of year 2022
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    result = []
    line = [y - 96 if y > 90 else y - 38 for y in  [ord(x) for x in [*line.strip()]]]

    return [line[0:int(len(line)/2)], line[int(len(line)/2):]]

def double_item_priority(data):
    items = []
    for line in data:
        intersection = set([x for x in line[0] if x in line[1]])
        for item in enumerate(intersection):
            items.append(item[1])
    return sum(items)

def badge_priority(data):
    items = []
    for x in range(0, len(data), 3):
        set1 = set([*data[x][0], *data[x][1]])
        set2 = set([*data[x + 1][0], *data[x + 1][1]])
        set3 = set([*data[x + 2][0], *data[x + 2][1]])
        intersection = [x for x in set1 if x in set2 and x in set3]
        for item in intersection:
            items.append(item)
    return sum(items)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = double_item_priority(data)

    # Part 2
    solution2 = badge_priority(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
