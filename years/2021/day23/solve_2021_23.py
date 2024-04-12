"""
Solution for day 23 of year 2021
"""

import os
import regex
from copy import deepcopy
from queue import PriorityQueue

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    row = 0
    result = [[],[],[],[]]
    for line in lines:
        check = regex.findall('#([ABCD])#([ABCD])#([ABCD])#([ABCD])#', line)
        if check:
            row += 1
            for pos, char in enumerate(check[0]):
                result[ord(char)-65].append([2 + pos * 2, row])

    return tuple(result)

def modify_input(data):
    tmp = tuple([[[y[0], y[1] if y[1] == 1 else 4] for y in x] for x in deepcopy(data)])
    tmp[0].append([8,2])
    tmp[0].append([6,3])
    tmp[1].append([6,2])
    tmp[1].append([4,3])
    tmp[2].append([4,2])
    tmp[2].append([8,3])
    tmp[3].append([2,2])
    tmp[3].append([2,3])
    return tmp

def least_energy(data):
    queue = PriorityQueue()
    bottom = max([max([y[1] for y in x]) for x in data])

    tmp = update_wants_move([[[y[0], y[1], True] for y in x] for x in data], bottom)
    seen = {
        stringify(tmp): 0
    }

    queue.put([0, tmp])

    cost = (1,10,100,1000)

    while queue.qsize():
        (moves, check) = queue.get()

        if sum([len([y[2] for y in x if y[2] == True]) for x in check]) == 0:
            return moves


        tmp = [[(y[0] ,y[1])for y in x] for x in check]
        occupied = [*tmp[0], *tmp[1], *tmp[2], *tmp[3]]
        for (idx, poslist) in enumerate(check):
            for posidx, pos in enumerate(poslist):
                if pos[2]:
                    if pos[1] == 0:
                        can_move_down = True
                        target_x = (idx+1)*2
                        for x in range(pos[0], target_x, 1 if target_x > pos[0] else -1):
                            if (x, 0) in occupied and x != pos[0]:
                                can_move_down = False
                                break
                        target_y = 1
                        for y in range(0, bottom + 1):
                            if (target_x, y) in occupied and (target_x, y) not in [(x[0], x[1]) for x in check[idx]]:
                                can_move_down = False
                                break
                            elif (target_x, y) not in occupied:
                                target_y = y
                        if can_move_down:
                            check2 = deepcopy(check)
                            check2[idx][posidx][0] = target_x
                            check2[idx][posidx][1] = target_y
                            checkmoves = (abs(pos[0] - target_x) + abs(pos[1] - target_y)) * cost[idx] + moves
                            stringified = stringify(check2)
                            if stringified not in seen or seen[stringified] > checkmoves:
                                seen[stringified] = checkmoves
                                check2 = update_wants_move(check2, bottom)
                                queue.put([checkmoves, check2])
                    else:
                        can_move_up = True
                        for y in range(pos[1] - 1, 0, -1):
                            if (pos[0], y) in occupied:
                                can_move_up = False
                                break
                        if can_move_up:
                            positions_to_add = []
                            #left
                            for x in range(pos[0]-1, -1, -1):
                                if (x,0) in occupied:
                                    break
                                if x not in (2,4,6,8):
                                    positions_to_add.append((x,0))
                            #right
                            for x in range(pos[0]+1, 11):
                                if (x,0) in occupied:
                                    break
                                if x not in (2,4,6,8):
                                    positions_to_add.append((x,0))

                            for position_to_add in positions_to_add:
                                check2 = deepcopy(check)
                                check2[idx][posidx][0] = position_to_add[0]
                                check2[idx][posidx][1] = position_to_add[1]
                                checkmoves = (abs(pos[0] - position_to_add[0]) + abs(pos[1] - position_to_add[1])) * cost[idx] + moves
                                stringified = stringify(check2)
                                if stringified not in seen or seen[stringified] > checkmoves:
                                    seen[stringified] = checkmoves
                                    check2 = update_wants_move(check2, bottom)
                                    queue.put([checkmoves, check2])

def stringify(data):
    return "|-|".join(["|".join(sorted([str(y[0]) + "_" + str(y[1]) for y in x])) for x in data])


def update_wants_move(data, bottom):
    data = deepcopy(data)
    for (posnum, poslist) in enumerate(data):
        for ypos in range(bottom, 0, -1):
            check = [pos for pos in poslist if pos[0] == (posnum + 1) * 2 and pos[1] == ypos]
            if len(check) == 1:
                check[0][2] = False
            else:
                break
    return data

def solve(data):
    """Solve the puzzle for the given input"""

    data_modified = modify_input(data)

    # Part 1
    solution1 = least_energy(data)

    # Part 2
    solution2 = least_energy(data_modified)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
