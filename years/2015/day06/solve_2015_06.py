"""
Solution for day 06 of year 2015
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    if line[0:7] == 'turn on':
        tmp = [[int(y) for y in x.split(',')] for x in line[8:].split(' through ')]
        return ('on', tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1])
    elif line[0:6] == 'toggle':
        tmp = [[int(y) for y in x.split(',')] for x in line[7:].split(' through ')]
        return ('toggle', tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1])
    elif line[0:8] == 'turn off':
        tmp = [[int(y) for y in x.split(',')] for x in line[9:].split(' through ')]
        return ('off', tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1])
    else:
        print (line)
        exit()
    return line

def count_lights(data):
    lights = []
    for x in range(1000):
        lights.append([0]*1000)
    for command in data:
        if command[0] == 'on':
            for y in range(command[2], command[4] + 1):
                for x in range(command[1], command[3] + 1):
                    lights[y][x] = 1
        elif command[0] == 'off':
            for y in range(command[2], command[4] + 1):
                for x in range(command[1], command[3] + 1):
                    lights[y][x] = 0
        elif command[0] == 'toggle':
            for y in range(command[2], command[4] + 1):
                for x in range(command[1], command[3] + 1):
                    lights[y][x] = (lights[y][x] + 1) % 2
    return sum([sum(x) for x in lights])

def total_brightness(data):
    lights = []
    for x in range(1000):
        lights.append([0]*1000)
    for command in data:
        if command[0] == 'on':
            for y in range(command[2], command[4] + 1):
                for x in range(command[1], command[3] + 1):
                    lights[y][x] += 1
        elif command[0] == 'off':
            for y in range(command[2], command[4] + 1):
                for x in range(command[1], command[3] + 1):
                    lights[y][x] = max(0, lights[y][x] - 1)
        elif command[0] == 'toggle':
            for y in range(command[2], command[4] + 1):
                for x in range(command[1], command[3] + 1):
                    lights[y][x] = lights[y][x] + 2
    return sum([sum(x) for x in lights])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_lights(data)

    # Part 2
    solution2 = total_brightness(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

