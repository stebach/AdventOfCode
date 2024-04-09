"""
Solution for day 22 of year 2021
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().replace(' x=',' ').replace('..', ' ').replace(',y=',' ').replace(',z=',' ').split(' ')
    return tuple([line[0] == 'on', *[int(x) for x in line[1:]]])

def count_on(data, initialization=False):
    cubes = []
    for new_cube in data:
        if initialization:
            new_cube = ([*new_cube])
            if new_cube[1] > 50 or new_cube[2] < -50 or new_cube[3] > 50 or new_cube[4] < -50 or new_cube[5] > 50 or new_cube[6] < -50:
                continue
        intersecting = []
        for old_cube in cubes:
            if new_cube[1] <= old_cube[2] and new_cube[2] >= old_cube[1] and new_cube[3] <= old_cube[4] and new_cube[4] >= old_cube[3] and new_cube[5] <= old_cube[6] and new_cube[6] >= old_cube[5]:
                intersecting.append(old_cube)
        if len(intersecting) > 0:
            for split_cube in intersecting:
                cubes.remove(split_cube)
                cut_and_add(cubes, split_cube, new_cube)
        if new_cube[0]:
            cubes.append(new_cube)

    total = 0
    for cube in cubes:
        if cube[0]:
            total += (cube[2] - cube[1] + 1) * (cube[4] - cube[3] + 1) * (cube[6] - cube[5] + 1)
    return total

def cut_and_add(cubes, split_cube, new_cube):
    result = [split_cube]
    if new_cube[2] <= split_cube[2]:
        cut_at(new_cube[2], 1, result)
    if new_cube[1] >= split_cube[1]:
        cut_at(new_cube[1] - 1, 1, result)
    if new_cube[4] <= split_cube[4]:
        cut_at(new_cube[4], 3, result)
    if new_cube[3] >= split_cube[3]:
        cut_at(new_cube[3] - 1, 3, result)
    if new_cube[6] <= split_cube[6]:
        cut_at(new_cube[6], 5, result)
    if new_cube[5] >= split_cube[5]:
        cut_at(new_cube[5] - 1, 5, result)
    
    intersecting = None
    for check in result:
        if new_cube[1] <= check[2] and new_cube[2] >= check[1] and new_cube[3] <= check[4] and new_cube[4] >= check[3] and new_cube[5] <= check[6] and new_cube[6] >= check[5]:
            if intersecting == None:
                intersecting = check
            else:
                print("ERR 1")
                exit()

    if intersecting == None:
        print("ERR 2")
        exit()

    result.remove(intersecting)
    cubes.extend(result)


def cut_at(pos, idx, result):
    new_result = []
    while len(result) > 0:
        current = result.pop(0)
        if current[idx] <= pos and current[idx + 1] >= pos:
            tmp = [*current]
            tmp[idx] = pos + 1
            if tmp[idx] <= tmp[idx+1]:
                new_result.append(tmp)
            tmp = [*current]
            tmp[idx + 1] = pos
            if tmp[idx] <= tmp[idx+1]:
                new_result.append(tmp)
        else:
            new_result.append(current)
    result.extend(new_result)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_on(data, True)

    # Part 2
    solution2 = count_on(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
