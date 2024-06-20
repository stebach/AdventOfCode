"""
Solution for day 07 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = []
    elements = {}
    possible_root = []
    for line in lines:
        line = line.strip().split(' -> ')
        name, weight = line[0].split(' ')
        possible_root.append(name)
        weight = int(weight[1:-1])
        elements[name] = {
            "name": name,
            "weight": weight,
            "sub": line[1].split(', ') if len(line) > 1 else []
        }
    for key, element in elements.items():
        for s in element['sub']:
            possible_root.remove(s)
        element['sub'] = [elements[x] for x in element['sub']]

    return elements[possible_root[0]]

def get_weight_to_balance(data):
    calc_weight(data)
    return get_balance_weight(data)

def get_balance_weight(data):
    minw = min(data['subweights'])
    maxw = max(data['subweights'])
    if minw != maxw:
        if data['subweights'].count(minw) == 1:
            balance = get_balance_weight(data['sub'][data['subweights'].index(minw)])
            if balance == 0:
                return data['sub'][data['subweights'].index(minw)]['weight'] + maxw - minw
            else:
                return balance
        elif data['subweights'].count(maxw) == 1:
            balance = get_balance_weight(data['sub'][data['subweights'].index(maxw)])
            if balance == 0:
                return data['sub'][data['subweights'].index(maxw)]['weight'] - maxw + minw
            else:
                return balance
        return False
    else:
        return 0

def calc_weight(data):
    if 'subweights' not in data:
        data['subweights'] = [calc_weight(x) for x in data['sub']]
    return data['weight'] + sum(data['subweights'])


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = data['name']

    # Part 2
    solution2 = get_weight_to_balance(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
