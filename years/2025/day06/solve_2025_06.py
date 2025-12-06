"""
Solution for day 06 of year 2025
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    math_problems = []
    for row in lines:
        columns = row.split()
        for col_num in range(len(columns)):
            if len(math_problems) <= col_num:
                math_problems.append({
                    'numbers': {
                        'part1': [],
                        'part2': []
                    },
                    'operation': None
                })
            if columns[col_num] in ('*', '+'):
                math_problems[col_num]['operation'] = columns[col_num]
            else:
                math_problems[col_num]['numbers']['part1'].append(int(columns[col_num]))

    problem_num = 0
    for col_num in range(len(lines[0])):
        number_found = False
        current_number = ''
        for row_num in range(len(lines) - 1):
            value = lines[row_num][col_num]
            if value not in (' ', '\n'):
                current_number = current_number + value
                number_found = True
        if not number_found:
            problem_num += 1
        else:
            math_problems[problem_num]['numbers']['part2'].append(int(current_number))


    return tuple(math_problems)

def calc(data):

    result1 = 0
    result2 = 0
    for problem in data:
        if problem['operation'] == '*':
            res = 1
            for number in problem['numbers']['part1']:
                res = res * number
            res2 = 1
            for number in problem['numbers']['part2']:
                res2 = res2 * number
        elif problem['operation'] == '+':
            res = 0
            for number in problem['numbers']['part1']:
                res = res + number
            res2 = 0
            for number in problem['numbers']['part2']:
                res2 = res2 + number
        result1 += res
        result2 += res2

    return result1, result2


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1 & 2
    solution1, solution2 = calc(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

