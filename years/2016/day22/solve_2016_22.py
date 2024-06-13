"""
Solution for day 22 of year 2016
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = []
    for line in lines:
        res = regex.findall(r'\/node-x([0-9]+)-y([0-9]+)\s+([0-9]+)T\s+([0-9]+)T\s+([0-9]+)T', line)
        if res:
            result.append(tuple([int(x) for x in res[0]]))
    return tuple(result)

def count_pairs(data):
    count = set()
    for line in data:
        if line[3] == 0:
            continue
        matches = [x for x in data if x[4] >= line[3] and (x[0] != line[0] or x[1] != line[1])]
        for match in matches:
            count.add(tuple(sorted([line, match])))
    return len(count)

def fewest_steps(data):
    target_x = max([x[0] for x in data])
    data = [[y for y in x] for x in data]
    steps = 0
    while target_x != 0:
        closest_empty = find_closest_empty(((target_x - 1, 0),), data, (target_x, 0))
        steps += len(closest_empty)
        data = do_moves(((target_x, 0), ) + closest_empty, data)
        target_x -= 1
    return steps

def do_moves(moves, data):
    move = len(moves) - 1
    while move > 0:
        to_data = [x[0] for x in enumerate(data) if x[1][0] == moves[move][0] and x[1][1] == moves[move][1]][0]
        from_data = [x[0] for x in enumerate(data) if x[1][0] == moves[move - 1][0] and x[1][1] == moves[move - 1][1]][0]
        amount = data[from_data][3]

        data[from_data][4] += amount
        data[from_data][3] = 0
        data[to_data][3] += amount
        data[to_data][4] -= amount

        move -= 1
    return data

def find_closest_empty(coords, data, ignore):
    directions = ((1,0),(-1,0), (0,1), (0,-1))
    max_x = max([x[0] for x in data])
    max_y = max([x[1] for x in data])
    queue = [coords]
    seen = set()
    while len(queue) > 0:
        entry = queue.pop(0)
        entry_data = [x for x in data if x[0] == entry[-1][0] and x[1] == entry[-1][1]][0]

        for direction in directions:
            if direction[0] + entry[-1][0] >= 0 and direction[0] + entry[-1][0] <= max_x and direction[1] + entry[-1][1] >= 0 and direction[1] + entry[-1][1] <= max_y and (direction[0] + entry[-1][0],direction[1] + entry[-1][1]) != ignore:
                if (direction[0] + entry[-1][0],direction[1] + entry[-1][1]) not in entry and (direction[0] + entry[-1][0],direction[1] + entry[-1][1]) not in seen:
                    seen.add((direction[0] + entry[-1][0],direction[1] + entry[-1][1]))
                    to_check = [x for x in data if x[0] == direction[0] + entry[-1][0] and x[1] == direction[1] + entry[-1][1]][0]
                    if to_check[2] >= entry_data[3]:
                        if to_check[4] >= entry_data[3]:
                            return entry + ((direction[0] + entry[-1][0],direction[1] + entry[-1][1]),)
                        else:
                            queue.append(entry + ((direction[0] + entry[-1][0],direction[1] + entry[-1][1]),))

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_pairs(data)

    # Part 2
    solution2 = fewest_steps(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

