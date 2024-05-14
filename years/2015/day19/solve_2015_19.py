"""
Solution for day 19 of year 2015
"""

import os
from queue import PriorityQueue

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    transformations = {}
    while len(lines) > 0:
        line = lines.pop(0).strip()
        if line == '':
            break
        parts = line.split(' => ')
        if parts[0] not in transformations:
            transformations[parts[0]] = []
        transformations[parts[0]].append(parts[1])
    return (
        dict([[x, tuple(transformations[x])] for x in transformations]),
        lines.pop(0).strip()
    )

def count_distinct_molecules(data):
    return len(get_distinct_molecules(data))

def get_distinct_molecules(data):
    initial = data[1]
    molecules = set()
    for key in data[0]:
        parts = initial.split(key)
        amount = len(parts)
        for replacement in data[0][key]:
            for i in range(amount - 1):
                enum = enumerate(parts)
                molecules.add("".join([x[1] + (replacement if x[0] == i else key) for x in enum])[:-len(key)])
    return molecules

def count_steps_to_create(data):
    new_dict = dict()
    for key in data[0]:
        for val in data[0][key]:
            if not val in new_dict:
                new_dict[val] = []
            new_dict[val].append(key)
    queue = PriorityQueue()
    queue.put((len(data[1]),0,data[1]))
    seen = set([data[1]])
    while True:
        entry = queue.get()
        if entry[2] == 'e':
            return entry[1]
        next_entries = get_distinct_molecules((new_dict, entry[2]))
        for x in next_entries:
            if x not in seen:
                seen.add(x)
                queue.put((len(x), entry[1] + 1, x))

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_distinct_molecules(data)

    # Part 2
    solution2 = count_steps_to_create(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
