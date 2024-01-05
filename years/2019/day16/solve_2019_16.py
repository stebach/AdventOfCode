"""
Solution for day 16 of year 2019
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def parse_line(line):
    line = line.strip()
    return line

def parse_lines(lines):
    return [x for x in lines]

def get_pattern(no):
    return [0] * (no + 1) + [1] * (no + 1) + [0] * (no + 1) + [-1] * (no + 1)

def run_phase(input):
    output = ''
    for x in range(len(input)):
        pattern = get_pattern(x)
        output += str(sum([int(char) * pattern[(pos+1) % len(pattern)] for pos, char in enumerate(input)]))[-1]
    return output

def run_phases(data, times):
    for x in range(times):
        data = run_phase(data)
    return data

def real_signal(data):
    start = int(data[0:7])
    data *= 10000
    relevant_part = [int(x) for x in [* data][start:]]

    for y in range(100):
        for x in range(len(relevant_part)-1):
            relevant_part[len(relevant_part) - x - 2] = (relevant_part[len(relevant_part) - x - 2] + relevant_part[len(relevant_part) - x - 1]) % 10

    return "".join([str(x) for x in relevant_part[0:8]])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = run_phases(data, 100)[0:8]

    # Part 2
    solution2 = real_signal(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
