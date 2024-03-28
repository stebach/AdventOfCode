"""
Solution for day 10 of year 2021
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def get_corrupted_score(data):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    return sum([points[y[1]] for y in [analyze(x) for x in data] if y[0] == 'c'])

def get_incomplete_score(data):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    lines = [y[1] for y in [analyze(x) for x in data] if y[0] == 'i']
    scores = []
    for line in lines:
        score = 0
        for char in line:
            score = score * 5 + points[char]
        scores.append(score)
    scores.sort()
    return scores[int((len(scores)-1)/2)]

def analyze(data):
    chars = [*data]
    buffer = []
    for char in chars:
        if char in ['[','(','<','{']:
            buffer.append(char)
        else:
            if abs(ord(char) - ord(buffer[-1])) < 3:
                buffer.pop()
            else:
                return ('c',char)
    result = []
    while len(buffer) > 0:
        char = buffer.pop()
        if char == '(':
            result.append(')')
        else:
            result.append(chr(ord(char)+2))

    return ('i', result)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_corrupted_score(data)

    # Part 2
    solution2 = get_incomplete_score(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

