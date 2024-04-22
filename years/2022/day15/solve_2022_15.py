"""
Solution for day 15 of year 2022
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    pattern = r'x=([\-0-9]+), y=([\-0-9]+)'
    result = regex.findall(pattern, line)
    return ((int(result[0][0]), int(result[0][1])), (int(result[1][0]), int(result[1][1])), abs(int(result[0][0]) - int(result[1][0])) + abs(int(result[0][1]) - int(result[1][1])))

def invalid_beacon_positions_on_line(data, line = 2000000):
    invalid_positions = set([])

    for sensor in data:
        distance = abs(sensor[0][1] - line)
        if distance > sensor[2]:
            continue
        invalid_positions.add(sensor[0][0])
        for x in range(1, abs(sensor[2] - distance) + 1):
            invalid_positions.add(sensor[0][0] + x)
            invalid_positions.add(sensor[0][0] - x)

    beacon_x = set([x[1][0] for x in data if x[1][1] == line])
    for bx in beacon_x:
        if bx in invalid_positions:
            invalid_positions.remove(bx)

    return len(invalid_positions)

def find_beacon_distress_frequency(data, max_coord = 4000000):
    for y in range(0, max_coord + 1):
        x = 0
        while x < max_coord + 1:
            found = True
            for sensor in data:
                distance = abs(sensor[0][0] - x) + abs(sensor[0][1] - y)
                if distance <= sensor[2]:
                    x = sensor[0][0] + (sensor[2] - abs(sensor[0][1] - y))
                    found = False
                    break
            
            if found:
                return x * 4_000_000 + y
            
            x += 1
    return 0

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = invalid_beacon_positions_on_line(data)

    # Part 2
    solution2 = find_beacon_distress_frequency(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
