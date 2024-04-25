"""
Solution for day 19 of year 2022
"""

import os
import regex
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    result = regex.findall(r'^Blueprint ([0-9]+): Each ore robot costs ([0-9]+) ore\. Each clay robot costs ([0-9]+) ore\. Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay\. Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian\.$', line)
    return tuple([int(x) for x in result[0]])

def get_quality_level(data):
    result = 0
    for line in data:
        result += get_best_result(line, 24) * line[0]
    return result

def get_best_result(data, minutes):
    idx_id = 0
    idx_ore_robot_ore_cost = 1
    idx_clay_robot_ore_cost = 2
    idx_obsidian_robot_ore_cost = 3
    idx_obsidian_robot_clay_cost = 4
    idx_geode_robot_ore_cost = 5
    idx_geode_robot_obsidian_cost = 6

    idx_blueprint = 0
    idx_ore_robots = 1
    idx_ore = 2
    idx_clay_robots = 3
    idx_clay = 4
    idx_obsidian_robots = 5
    idx_obsidian = 6
    idx_geode_robots = 7
    idx_geodes = 8

    queue = set([(data,1,0,0,0,0,0,0,0)])
    for i in range(minutes):
        new_queue = set([])
        for next_state in queue:
            check = 0
            if next_state[idx_obsidian] >= next_state[idx_blueprint][idx_geode_robot_obsidian_cost] and next_state[idx_ore] >= next_state[idx_blueprint][idx_geode_robot_ore_cost]:
                new_queue.add((
                    next_state[idx_blueprint],
                    next_state[idx_ore_robots],
                    next_state[idx_ore] + next_state[idx_ore_robots] - next_state[idx_blueprint][idx_geode_robot_ore_cost],
                    next_state[idx_clay_robots],
                    next_state[idx_clay] + next_state[idx_clay_robots],
                    next_state[idx_obsidian_robots],
                    next_state[idx_obsidian] + next_state[idx_obsidian_robots] - next_state[idx_blueprint][idx_geode_robot_obsidian_cost],
                    next_state[idx_geode_robots] + 1,
                    next_state[idx_geodes] + next_state[idx_geode_robots],
                ))
                check += 1
            if next_state[idx_clay] >= next_state[idx_blueprint][idx_obsidian_robot_clay_cost] and next_state[idx_ore] >= next_state[idx_blueprint][idx_obsidian_robot_ore_cost]:
                new_queue.add((
                    next_state[idx_blueprint],
                    next_state[idx_ore_robots],
                    next_state[idx_ore] + next_state[idx_ore_robots] - next_state[idx_blueprint][idx_obsidian_robot_ore_cost],
                    next_state[idx_clay_robots],
                    next_state[idx_clay] + next_state[idx_clay_robots] - next_state[idx_blueprint][idx_obsidian_robot_clay_cost],
                    next_state[idx_obsidian_robots] + 1,
                    next_state[idx_obsidian] + next_state[idx_obsidian_robots],
                    next_state[idx_geode_robots],
                    next_state[idx_geodes] + next_state[idx_geode_robots],
                ))
                check += 1
            if next_state[idx_ore] >= next_state[idx_blueprint][idx_clay_robot_ore_cost]:
                new_queue.add((
                    next_state[idx_blueprint],
                    next_state[idx_ore_robots],
                    next_state[idx_ore] + next_state[idx_ore_robots] - next_state[idx_blueprint][idx_clay_robot_ore_cost],
                    next_state[idx_clay_robots] + 1,
                    next_state[idx_clay] + next_state[idx_clay_robots],
                    next_state[idx_obsidian_robots],
                    next_state[idx_obsidian] + next_state[idx_obsidian_robots],
                    next_state[idx_geode_robots],
                    next_state[idx_geodes] + next_state[idx_geode_robots],
                ))
                check += 1
            if next_state[idx_ore] >= next_state[idx_blueprint][idx_ore_robot_ore_cost]:
                new_queue.add((
                    next_state[idx_blueprint],
                    next_state[idx_ore_robots] + 1,
                    next_state[idx_ore] + next_state[idx_ore_robots] - next_state[idx_blueprint][idx_ore_robot_ore_cost],
                    next_state[idx_clay_robots],
                    next_state[idx_clay] + next_state[idx_clay_robots],
                    next_state[idx_obsidian_robots],
                    next_state[idx_obsidian] + next_state[idx_obsidian_robots],
                    next_state[idx_geode_robots],
                    next_state[idx_geodes] + next_state[idx_geode_robots],
                ))
                check += 1
            if check < 4:
                new_queue.add((
                    next_state[idx_blueprint],
                    next_state[idx_ore_robots],
                    next_state[idx_ore] + next_state[idx_ore_robots],
                    next_state[idx_clay_robots],
                    next_state[idx_clay] + next_state[idx_clay_robots],
                    next_state[idx_obsidian_robots],
                    next_state[idx_obsidian] + next_state[idx_obsidian_robots],
                    next_state[idx_geode_robots],
                    next_state[idx_geodes] + next_state[idx_geode_robots],
                ))
        queue.clear()

        minute = minutes - 1 - i

        if len(new_queue) > 100_000:
            new_queue = sorted(list(new_queue), key=lambda y: y[idx_geode_robots] * 1_000_000 + y[idx_obsidian_robots] * 1_000 + y[idx_clay_robots], reverse=True)[0:100_000]
        
        queue.update(new_queue)

    result = sorted(list(queue), key=lambda x: x[idx_geodes], reverse=True)
    return result[0][idx_geodes]

def get_geodes_of_first_blueprints(data, number_of_blueprints):
    result = 1
    for line in data[0:3]:
        result *= get_best_result(line, 32)
    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_quality_level(data)

    # Part 2
    solution2 = get_geodes_of_first_blueprints(data, 3)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
