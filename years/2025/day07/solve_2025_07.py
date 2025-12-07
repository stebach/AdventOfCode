"""
Solution for day 07 of year 2025
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {
        'start': None,
        'splitters': [],
        'height': 0,
    }
    for row in range(len(lines)):
        line = lines[row].strip()
        if len(line) == 0:
            continue
        result['height'] = result['height'] + 1
        for col in range(len(line)):
            char = line[col]
            if char == 'S':
                result['start'] = (col, row)
            elif char == '^':
                result['splitters'].append((col, row))
    
    result['splitters'] = tuple(result['splitters'])

    return result

def split_timeline(timelines, position, count):
    if timelines.get(position) is None:
        timelines[position] = count
    else:
        timelines[position] += count

def emulate_tachion(data):
    rays = set(((data['start'][0], data['start'][1]+1),))
    pos = data['start'][1]+1
    last_rays = rays
    splitters_hit = set([])
    timelines = { (data['start'][0], data['start'][1]+1): 1 }
    while pos < data['height']:
        newrays = set([])
        new_timelines = {}
        for ray in last_rays:
            next_pos = (ray[0], ray[1]+1)
            if next_pos in data['splitters']:
                splitters_hit.add(next_pos)
                newrays.add((ray[0]-1, pos+1))
                newrays.add((ray[0]+1, pos+1))
                split_timeline(new_timelines, (ray[0]-1, pos+1), timelines[ray])
                split_timeline(new_timelines, (ray[0]+1, pos+1), timelines[ray])
            else:
                split_timeline(new_timelines, next_pos, timelines[ray])
                newrays.add(next_pos)
        last_rays = newrays
        rays.update(newrays)
        pos = pos + 1
        timelines = new_timelines
    
    return len(splitters_hit), sum(new_timelines.values())


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1 & Part 2
    solution1, solution2 = emulate_tachion(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
