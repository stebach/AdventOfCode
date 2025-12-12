"""
Solution for day 12 of year 2025
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {
        'shapes': {

        },
        'areas': [

        ]
    }

    shape_lines = []
    shape_id = None
    for line in lines:
        line = line.strip()
        if not line:
            if shape_id is not None:
                result['shapes'][shape_id] = shape_lines
                shape_id = None
                shape_lines = []
            continue
        if line.endswith(':'):
            shape_id = int(line[:-1])
            shape_lines = []
            continue
        elif ':' in line:
            area_part = line.split(': ')
            dimensions = tuple(map(int, area_part[0].split('x')))
            shape_ids = list(map(int, area_part[1].split(' ')))
            result['areas'].append((dimensions[0], dimensions[1], shape_ids))
        else:
            shape_lines.append(line)
    result['areas'] = tuple(result['areas'])
    return result

def can_fit_shapes(shapes, area):
    width, height, shape_ids = area

    total_size = 0
    for shape_id, count in enumerate(shape_ids):
        total_size += count * sum([x.count('#') for x in shapes[shape_id]])
    if total_size > width * height:
        return False
    return True

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum(1 for area in data['areas'] if can_fit_shapes(data['shapes'], area))
    return solution1, None

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

