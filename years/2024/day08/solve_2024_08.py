"""
Solution for day 08 of year 2024
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {
        'h': 0,
        'w': 0,
        'antennas': {}
    }

    for y, line in enumerate(lines):
        line = line.strip()
        if len(line) == 0:
            break
        result['h'] = y + 1
        result['w'] = len(line)
        for x, char in enumerate(line):
            if char == '.':
                continue
            if char not in result['antennas']:
                result['antennas'][char] = []
            result['antennas'][char].append((x, y))
    return result

def unique_antinodes(data, with_resonant_harmonics=False):
    unique_antinodes = set()

    for antenna, positions in data['antennas'].items():
        for position1 in range(len(positions) - 1):
            for position2 in range(position1 + 1, len(positions)):
                add_antinodes(positions[position1], positions[position2], unique_antinodes, data['w'], data['h'], with_resonant_harmonics)
                add_antinodes(positions[position2], positions[position1], unique_antinodes, data['w'], data['h'], with_resonant_harmonics)

    return unique_antinodes

def add_antinodes(position1, position2, unique_antinodes, w, h, with_resonant_harmonics):
    direction1 = (position1[0] - position2[0], position1[1] - position2[1])
    x = position1[0] + direction1[0]
    y = position1[1] + direction1[1]

    while x in range(w) and y in range(h):
        unique_antinodes.add((x, y))
        x += direction1[0]
        y += direction1[1]
        if not with_resonant_harmonics:
            break
    
    if with_resonant_harmonics:
        unique_antinodes.add(position1)
        unique_antinodes.add(position2)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = len(unique_antinodes(data))

    # Part 2
    solution2 = len(unique_antinodes(data, True))
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
