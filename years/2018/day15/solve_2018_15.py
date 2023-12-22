"""
Solution for day 15 of year 2018
"""

import os
from queue import PriorityQueue
import copy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    walls = [];
    units = [];
    for y in range(len(lines)):
        for x in range(len(lines[y].strip())):
            if lines[y][x] == '#':
                walls.append((y,x))
            elif lines[y][x] in 'GE':
                units.append([(y,x),lines[y][x], 3, 200])
            elif lines[y][x] not in '.':
                print("CHAR: " + lines[y][x])
    return {
        'walls': tuple(walls),
        'units': units
    }

def get_result(data, stop_if_elf_killed=False):
    directions = ((-1,0), (0,-1), (0,1), (1,0))
    queue = PriorityQueue()
    rounds = 0

    while True:
        for unit in [x for x in data['units'] if x[3] > 0]:
            queue.put(unit)

        while not queue.empty():
            unit = queue.get()
            if unit[3] < 1:
                continue

            # targets
            targets = [y for y in data['units'] if y[1] != unit[1] and y[3] > 0]
            if len(targets) == 0:
                return (data, rounds)

            target_list = []
            for target in targets:
                for direction in directions:
                    movement_target = (target[0][0] + direction[0], target[0][1] + direction[1])
                    if movement_target == unit[0]:
                        target_list.append(movement_target)
                    elif movement_target not in data['walls'] and movement_target not in [y[0] for y in data['units'] if y[3] > 0]:
                        target_list.append(movement_target)
            

            min_distance = 100000000000000
            movement_targets = PriorityQueue()
            movement_count = 0
            if unit[0] not in target_list:
                to_scan = PriorityQueue()
                to_scan.put((0, unit[0], []))
                visited = set()
                while not to_scan.empty():
                    check = to_scan.get()
                    for direction in directions:
                        pos = (check[1][0] + direction[0], check[1][1] + direction[1])
                        if pos in target_list:
                            min_distance = check[0]+1
                            movement_targets.put((check[0]+1, pos, check[2] + [pos]))
                            movement_count += 1
                        else:
                            if pos not in data['walls'] and pos not in [y[0] for y in data['units'] if y[3] > 0] and pos not in visited and check[0] < min_distance:
                                visited.add(pos)
                                to_scan.put((check[0]+1, pos, check[2] + [pos]))

            if not movement_targets.empty():
                unit[0] = movement_targets.get()[2][0]

            attack_targets = PriorityQueue()
            for direction in directions:
                check_pos = (unit[0][0] + direction[0], unit[0][1] + direction[1])
                check = [y for y in targets if y[0] == check_pos]
                if len(check) > 0:
                    attack_targets.put((check[0][3], check[0]))

            if not attack_targets.empty():
                final_target = attack_targets.get()
                final_target[1][3] -= unit[2]
                if stop_if_elf_killed and final_target[1][1] == 'E' and final_target[1][3] < 1:
                    return (data, None)

        rounds += 1

def part1(data):
    """Solve part 1"""
    data_copy = copy.deepcopy(data)
    result, rounds = get_result(data_copy)
    return sum([x[3] for x in result['units'] if x[3] > 0] * rounds)

def part2(data):
    """Solve part 2"""
    data_copy = copy.deepcopy(data)
    elf_attack = 3
    result, rounds = get_result(data_copy, True)
    while rounds is None:
        elf_attack += 1
        data_copy = copy.deepcopy(data)
        for unit in data_copy['units']:
            if unit[1] == 'E':
                unit[2] = elf_attack
        result, rounds = get_result(data_copy, True)

    return sum([x[3] for x in result['units'] if x[3] > 0]) * rounds

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
