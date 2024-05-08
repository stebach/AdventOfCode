"""
Solution for day 14 of year 2015
"""

import os
import regex
import math

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = regex.findall(r'^([a-z]+) can fly ([0-9]+) km\/s for ([0-9]+) seconds?, but then must rest for ([0-9]+) seconds?\.$', line.strip(), regex.IGNORECASE)
    return (line[0][0], int(line[0][1]), int(line[0][2]), int(line[0][3]))

def get_distance(data, seconds):
    full_cycles = math.floor(seconds / (data[2] + data[3]))
    return full_cycles * (data[1] * data[2]) + min((seconds % (data[2] + data[3])), data[2]) * data[1]

def get_scores(data, seconds):
    score = [0] * len(data)
    for sec in range(seconds):
        dist = []
        for x in data:
            dist.append(get_distance(x, sec + 1))
        for x in range(len(data)):
            if dist[x] == max(dist):
                score[x] += 1
    return score


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = max([get_distance(x, 2503) for x in data])

    # Part 2
    solution2 = max(get_scores(data, 2503))
    print(solution2)
    exit()
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
