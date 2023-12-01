"""
Solution for day 02 of year 2018
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def part1(data):
    """Solve part 1"""
    score_data = tuple(map(get_score, data))
    return sum(tuple(map(lambda item: item[0], score_data))) * sum(tuple(map(lambda item: item[1], score_data)))

def get_score(item):
    two = 0
    three = 0
    for char in set([*item]):
        if item.count(char) == 2:
            two = 1
        if item.count(char) == 3:
            three = 1
    return tuple([two, three])

def part2(data):
    """Solve part 2"""
    min_diff_data = tuple([1000, '', ''])

    for pos1 in range(len(data) - 1):
        for pos2 in range(pos1 + 1, len(data)):
            string1 = [*data[pos1]]
            string2 = [*data[pos2]]
            common = []

            for pos3, char in enumerate(string1):
                if char == string2[pos3]:
                    common.append(char)

            diffs = len(string1) - len(common)
            if diffs < min_diff_data[0]:
                min_diff_data = tuple([diffs, data[pos1], data[pos2], common])

    return ''.join(min_diff_data[3])

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
