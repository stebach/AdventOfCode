"""
Solution for day 22 of year 2022
"""

import os
import regex
from math import cos, sin, radians

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = []
    grid = []
    while len(lines) > 0:
        line = lines.pop(0).rstrip()
        if len(line) == 0:
            max_grid_len = max([len(x) for x in grid])
            result.append(tuple([x.ljust(max_grid_len, ' ') for x in grid]))
            line = lines.pop(0).rstrip()
            res = regex.findall(r'([0-9]+|R|L)', line)
            result.append(tuple([-90 if x == 'R' else 90 if x == 'L' else int(x) for x in res]))

            for (y, line) in enumerate(result[0]):
                for (x, char) in enumerate(line):
                    if char == '.':
                        result.append((x,y))
                        break
                if len(result) == 3:
                    break
        else:
            grid.append(line)
    return tuple(result)

def get_password(data, cube=False):
    x = data[2][0]
    y = data[2][1]

    isTurn = False
    direction = [ 1, 0 ]

    for instruction in data[1]:
        if isTurn:
            cosVal = cos(radians(instruction))
            sinVal = sin(radians(instruction))
            newX = direction[0] * cosVal - direction[1] * sinVal
            newY = direction[0] * sinVal - direction[1] * cosVal
            direction = [ int(newX), int(newY) ]
        else:
            for i in range(instruction):
                newDirection = [direction[0], direction[1]]
                newX = x + newDirection[0]
                newY = y - newDirection[1]
                fixedData = fixData(data[0], newX, newY, direction, cube)

                newX = fixedData[0]
                newY = fixedData[1]
                newDirection[0] = fixedData[2]
                newDirection[1] = fixedData[3]

                if data[0][newY][newX] == '.':
                    x = newX
                    y = newY
                    direction[0] = newDirection[0]
                    direction[1] = newDirection[1]
                elif data[0][newY][newX] == '#':
                    break
                else:
                    print(data[0][newY][newX])
                    print("ERR")
                    exit()

        isTurn = not isTurn

    facing = 0
    if direction[1] == -1:
        facing = 1
    elif direction[0] == -1:
        facing = 2
    elif direction[1] == 1:
        facing = 3

    return 1000 * (y +  1) + 4 * (x +  1) + facing

def fixData(grid, x, y, direction, cube):
    newDirection = [direction[0], direction[1]]
    height = len(grid)
    width = len(grid[0])
    if height <= y:
        y = 0
    elif y < 0:
        y = height - 1
    if width <= x:
        x = 0
    elif x < 0:
        x = width - 1
    if not cube:
        while grid[y][x] == ' ':
            fixedData = fixData(grid, x + direction[0], y - direction[1], direction, cube)
            x = fixedData[0]
            y = fixedData[1]
    else:
        side = int(width / 4) if width > height else int(height / 4)
        if grid[y][x] == ' ':
            if newDirection[0] == -1:
                # left
                if y < side:
                    x = 0
                    y = 3 * side - 1 - y
                    newDirection[0] = 1
                elif y < 100:
                    x = y - 50
                    y = 100
                    newDirection[0] = 0
                    newDirection[1] = -1
                elif y < 150:
                    x = 50
                    y = 149 - y
                    newDirection[0] = 1
                elif y < 200:
                    x = y - 100
                    y = 0
                    newDirection[0] = 0
                    newDirection[1] = -1
                else:
                    print('left')
                    exit()

            elif newDirection[0] == 1:
                # right
                if y < 50:
                    x = 99
                    y = 149 - y
                    newDirection[0] = -1
                elif y < 100:
                    x = y + side
                    y = 49
                    newDirection[0] = 0
                    newDirection[1] = 1
                elif y < 150:
                    y = 3 * side - 1 - y
                    x = 149
                    newDirection[0] = -1
                elif y < 200:
                    x = y - 100
                    y = 149
                    newDirection[0] = 0
                    newDirection[1] = 1
                else:
                    print('right')
                    exit()
            elif newDirection[1] == -1:
                # down
                if x < 50:
                    x += 2 * side
                elif x < 100:
                    y = 2 * side + x
                    x = 49
                    newDirection[0] = -1
                    newDirection[1] = 0
                elif x < 150:
                    y = x - side
                    x = 99
                    newDirection[0] = -1
                    newDirection[1] = 0
                else:
                    print("down")
                    exit()

            elif newDirection[1] == 1:
                # up
                if x < 50:
                    y = side + x
                    x = 50
                    newDirection[0] = 1
                    newDirection[1] = 0
                elif x < 100:
                    y = 2 * side + x
                    x = 0
                    newDirection[0] = 1
                    newDirection[1] = 0
                elif x < 150:
                    x -= 2 * side
                else:
                    print('up')
                    exit()

    return [x, y, newDirection[0], newDirection[1]]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_password(data)

    # Part 2
    solution2 = get_password(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
