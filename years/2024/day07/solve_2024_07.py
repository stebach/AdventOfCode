"""
Solution for day 07 of year 2024
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    parts = line.split(': ')
    return { 'test_value': int(parts[0]), 'numbers': tuple(map(int, parts[1].split())) }

def check_equation(equation, with_concatenation = False):
    operators = ('+', '*')
    if with_concatenation:
        operators += ('||',)
    results = [equation['numbers'][0]]
    for i in range(1, len(equation['numbers'])):
        new_results = []
        for result in results:
            for operator in operators:
                new_number = result
                if operator == '+':
                    new_number += equation['numbers'][i]
                elif operator == '*':
                    new_number *= equation['numbers'][i]
                elif operator == '||':
                    new_number = int(str(new_number) + str(equation['numbers'][i]))

                if new_number == equation['test_value'] and i == len(equation['numbers']) - 1:
                    return True
                if new_number <= equation['test_value']:
                    new_results.append(new_number)
        results = new_results

    return False

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([x['test_value'] for x in data if check_equation(x) == True])

    # Part 2
    solution2 = sum([x['test_value'] for x in data if check_equation(x, True) == True])
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
