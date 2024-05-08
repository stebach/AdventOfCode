"""
Solution for day 12 of year 2015
"""

import os
import json

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def get_sum(data, dict_val_to_ignore=None):
    obj = json.loads(data)
    return get_obj_sum(obj, dict_val_to_ignore)

def get_obj_sum(obj, dict_val_to_ignore=None):
    if isinstance(obj, list):
        return sum([get_obj_sum(x, dict_val_to_ignore) for x in obj])
    elif isinstance(obj, dict):
        if dict_val_to_ignore is not None and len([obj[x] for x in obj if obj[x] == dict_val_to_ignore]) > 0:
            return 0
        return sum([get_obj_sum(obj[x], dict_val_to_ignore) for x in obj])
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, str):
        return 0
    else:
        print("unknown type:")
        print(type(obj))
        print(obj)
        exit()

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_sum(data)

    # Part 2
    solution2 = get_sum(data, 'red')
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
