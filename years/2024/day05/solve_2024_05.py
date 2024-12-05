"""
Solution for day 05 of year 2024
"""

import os
from functools import cmp_to_key

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {
        'rules':{},
        'pages': []
    }
    parse_pages = False
    for line in lines:
        if parse_pages:
            pages = list(map(int, line.split(',')))
            result['pages'].append(pages)
        else:
            if line.strip() == '':
                parse_pages = True
            else:
                rule = [int(x) for x in line.split('|')]
                if rule[0] not in result['rules']:
                    result['rules'][rule[0]] = []
                result['rules'][rule[0]].append(rule[1])

    return result

def right_order(pages, rules):
    for i in range(len(pages)):
        if pages[i] in rules:
            for after in rules[pages[i]]:
                if after in pages[:i]:
                    return False
    return True

def get_sum_of_middle_page_numbers(pages):
    return sum([x[len(x) // 2] for x in pages])

def order(pages, rules):
    def sorted_pages(a, b):
        if a in rules and b in rules[a]:
            return -1
        if b in rules and a in rules[b]:
            return 1
        return 0
    return sorted(pages, key=cmp_to_key(sorted_pages))


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_sum_of_middle_page_numbers(
        [x for x in data['pages'] if right_order(x, data['rules'])]
    )

    # Part 2
    solution2 = get_sum_of_middle_page_numbers(
        [order(x, data['rules']) for x in data['pages'] if not right_order(x, data['rules'])]
    )

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

