"""
Solution for day 18 of year 2018
"""

import os
import numpy as np

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    return np.array([* "".join(lines).replace("\n",'')]).reshape(len(lines[0].strip()),len(lines))

def count_surrounding(data, x, y):
    subgrid = "".join(["".join(np.split(z, [max(0,x-1), min(len(z),x+2)])[1]) for z in np.split(data,[max(0,y-1),min(len(data),y+2)])[1]])
    return {
        '#':subgrid.count('#') - data[y][x].count('#'),
        '.':subgrid.count('.') - data[y][x].count('.'),
        '|':subgrid.count('|') - data[y][x].count('|'),
    }

def progress_minutes(data, minutes):
    history = []
    for _ in range(minutes):
        result = np.empty([len(data), len(data[0])],'U')
        for y in range(len(data)):
            for x in range(len(data[0])):
                count = count_surrounding(data, x, y)
                if data[y][x] == '.' and count['|'] > 2:
                    result[y][x] = '|'
                elif data[y][x] == '|' and count['#'] > 2:
                    result[y][x] = '#'
                elif data[y][x] == '#' and not (count['#'] > 0 and count['|'] > 0):
                    result[y][x] = '.'
                else:
                    result[y][x] = data[y][x]
        data = result
        check = "".join(["".join(z) for z in data])
        if check in history:
            steps = len(history) - history.index(check)
            return history[history.index(check) + ((minutes - (_ + 1)) % steps)]
        else:
            history.append(check)
    return data


def part1(data, minutes=10):
    """Solve part 1"""
    data = progress_minutes(data, minutes)
    lumberyards = sum([sum([1 for y in x if y == '#']) for x in data])
    wooded_acres = sum([sum([1 for y in x if y == '|']) for x in data])
    return lumberyards * wooded_acres

def part2(data):
    """Solve part 2"""
    return part1(data, 1_000_000_000)

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
