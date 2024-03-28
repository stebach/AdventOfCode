"""
Solution for day 09 of year 2021
"""

import os
import numpy as np

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return [int(x) for x in [*line.strip()]]

def find_low_point_risk_level(data):
    height = len(data)
    width = len(data[0])
    risk_level = 0
    for y in range(height):
        for x in range(width):
            values = [data[y-1][x] if y > 0 else 10,
                      data[y+1][x] if y < height - 1 else 10,
                      data[y][x-1] if x > 0 else 10,
                      data[y][x+1] if x < width - 1 else 10]
            if data[y][x] < min(values):
                risk_level += 1 + data[y][x]
    return risk_level

def find_basins(data):
    basins = []
    basinsdata = {}
    nextbasin = -1
    for rownum, row in enumerate(data):
        basinrow = []
        basins.append(basinrow)
        for colnum, col in enumerate(row):
            if col == 9:
                basinrow.append(9)
            else:
                currentbasin = nextbasin
                if rownum > 0 and basins[rownum-1][colnum] < 0:
                    currentbasin = basins[rownum-1][colnum]
                if colnum > 0 and basinrow[colnum-1] < 0 and basinrow[colnum-1] != currentbasin:
                    if currentbasin != nextbasin:
                        oldbasin = basinrow[colnum-1]
                        for pos in basinsdata[oldbasin]:
                            basins[pos[0]][pos[1]] = currentbasin
                            basinsdata[currentbasin].append(pos)
                        
                        del basinsdata[oldbasin]
                    else:
                        currentbasin = basinrow[colnum-1]
                if currentbasin == nextbasin:
                    nextbasin -= 1
                    basinsdata[currentbasin] = []
                basinsdata[currentbasin].append((rownum, colnum))
                basinrow.append(currentbasin)
    return {
        'grid': basins,
        'count': dict([(x, len(basinsdata[x])) for x in basinsdata]),
        'areas_by_size': sorted([len(basinsdata[x]) for x in basinsdata], reverse=True)
    }

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_low_point_risk_level(data)

    # Part 2
    basins = find_basins(data)
    solution2 = np.prod(basins['areas_by_size'][0:3])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
