"""
Solution for day 25 of year 2022
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def snafu(nr):
    result = 0
    for x in range(len(nr)):
        factor = pow(5,x)
        char = nr[-x-1]
        if char == '1':
            result += factor
        elif char == '2':
            result += factor * 2
        elif char == '-':
            result -= factor
        elif char == '=':
            result -= factor * 2
        elif char == '0':
            continue
        else:
            print(char)
            exit()
    return result

def to_snafu(nr):
    base5 = ""
    while nr:
        base5 = str(nr % 5) + base5
        nr = int(nr / 5)

    add = 0
    result = ""
    for x in range(len(base5)):
        factor = pow(5,x)
        char = base5[-x-1]

        number_to_add = add    
        if char == '1':
            number_to_add += 1
        elif char == '2':
            number_to_add += 2
        elif char == '3':
            number_to_add += 3
        elif char == '4':
            number_to_add += 4
        elif char == '0':
            number_to_add += 0
        else:
            print("char")
            print(char)
            exit()
        
        if number_to_add in (1,2,0):
            result = str(number_to_add) + result
            add = 0
        elif number_to_add == 3:
            result = "=" + result
            add = 1
        elif number_to_add == 4:
            result = "-" + result
            add = 1
        elif number_to_add == 5:
            result = "0" + result
            add = 1
        else:
            print("number to add")
            print(number_to_add)
            exit()

    if (add > 0):
        result = str(add) + result

    return result

def to_base_5(n):
    return s

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = to_snafu(sum([snafu(x) for x in data]))

    # Part 2
    solution2 = None

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))


