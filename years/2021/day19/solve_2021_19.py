"""
Solution for day 19 of year 2021
"""

import os
import math

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = []
    scannerLines = []
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            if line[0:3] == '---':
                scannerLines = []
                result.append([int(line[12:-4]), scannerLines])
            else:
                scannerLines.append([int(x) for x in line.split(',')])
    return result

def position_scanners(data):
    rotations = [
        [0,0,0],
        [0,0,90],
        [0,0,180],
        [0,0,270],

        [0,90,0],
        [0,90,90],
        [0,90,180],
        [0,90,270],

        [0,180,0],
        [0,180,90],
        [0,180,180],
        [0,180,270],

        [0,270,0],
        [0,270,90],
        [0,270,180],
        [0,270,270],

        [90,0,0],
        [90,0,90],
        [90,0,180],
        [90,0,270],

        [270,0,0],
        [270,0,90],
        [270,0,180],
        [270,0,270],
    ]
    positioned = [
        data.pop(0)
    ]
    positioned[0].append([0,0,0])
    while len(data) > 0:
        scanner = data.pop(0)
        found = None
        for positioned_scanner in positioned:
            for rotation in rotations:
                rotated_beacons = modifiy_beacons(scanner[1], 0, 0, 0, rotation[0], rotation[1], rotation[2])
                for point1 in range(0, len(rotated_beacons)-11):
                    for point2 in range(0, len(positioned_scanner[1])-11):
                        shift_x = positioned_scanner[1][point2][0] - rotated_beacons[point1][0]
                        shift_y = positioned_scanner[1][point2][1] - rotated_beacons[point1][1]
                        shift_z = positioned_scanner[1][point2][2] - rotated_beacons[point1][2]

                        matched_list = [y for y in [[x[0] + shift_x, x[1] + shift_y, x[2] + shift_z] for x in rotated_beacons] if y in positioned_scanner[1]]
                        if len(matched_list) > 11:
                            found = [
                                scanner[0],
                                [[x[0] + shift_x, x[1] + shift_y, x[2] + shift_z] for x in rotated_beacons],
                                [shift_x, shift_y, shift_z]
                            ]
                            break
                if found != None:
                    break
            if found != None:
                break
        if found != None:
            positioned.append(found)
        else:
            data.append(scanner)

    return positioned

def modifiy_beacons(beacons, shift_x, shift_y, shift_z, rotate_x, rotate_y, rotate_z):
    result = []
    for beacon in beacons:
        (local_x, local_y, local_z) = beacon
        if rotate_x > 0:
            pre_rotate_y = local_y
            pre_rotate_z = local_z
            local_y = int(round(math.cos(math.radians(rotate_x)) * pre_rotate_y - math.sin(math.radians(rotate_x)) * pre_rotate_z))
            local_z = int(round(math.sin(math.radians(rotate_x)) * pre_rotate_y + math.cos(math.radians(rotate_x)) * pre_rotate_z))

        if rotate_y > 0:
            pre_rotate_x = local_x
            pre_rotate_z = local_z
            local_x = int(round(math.cos(math.radians(rotate_y)) * pre_rotate_x + math.sin(math.radians(rotate_y)) * pre_rotate_z))
            local_z = int(round(-math.sin(math.radians(rotate_y)) * pre_rotate_x + math.cos(math.radians(rotate_y)) * pre_rotate_z))

        if rotate_z > 0:
            pre_rotate_x = local_x
            pre_rotate_y = local_y
            local_x = int(round(math.cos(math.radians(rotate_z)) * pre_rotate_x - math.sin(math.radians(rotate_z)) * pre_rotate_y))
            local_y = int(round(math.sin(math.radians(rotate_z)) * pre_rotate_x + math.cos(math.radians(rotate_z)) * pre_rotate_y))


        local_x += shift_x;
        local_y += shift_y;
        local_z += shift_z;

        result.append([local_x, local_y, local_z])
    return result

def count_beacons(data):
    all = []
    for x in data:
        all += x[1]
    return len(set([str(x[0]) + "_" + str(x[1]) + "_" + str(x[2]) for x in all]))

def max_scanner_distance(data):
    count = len(data)
    max_distance = 0
    for x in range(count - 1):
        for y in range(x+1, count):
            distance = abs(data[x][2][0] - data[y][2][0]) + abs(data[x][2][1] - data[y][2][1]) + abs(data[x][2][2] - data[y][2][2])
            if distance > max_distance:
                max_distance = distance
    return max_distance

def solve(data):
    """Solve the puzzle for the given input"""
    data = position_scanners(data)
    # Part 1
    solution1 = count_beacons(data)

    # Part 2
    solution2 = max_scanner_distance(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
