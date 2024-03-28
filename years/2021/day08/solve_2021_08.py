"""
Solution for day 08 of year 2021
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([tuple(x.split(' ')) for x in line.strip().split(" | ")])

def count_digits_with_unique_number_of_segments(data):
    return sum([sum([1 for y in x[1] if len(y) in [2,4,3,7]]) for x in data])

def output_sum(data):
    return sum([get_output(x) for x in data])

def get_output(data):
    digits = [sorted([*x]) for x in data[0]]
    mapping = {}
    reverse_mapping = {}
    while len(digits) > 0:
        check = digits.pop(0)
        if len(check) == 3:
            mapping["".join(check)] = 7
            reverse_mapping[7] = check
        elif len(check) == 4:
            mapping["".join(check)] = 4
            reverse_mapping[4] = check
        elif len(check) == 2:
            mapping["".join(check)] = 1
            reverse_mapping[1] = check
        elif len(check) == 7:
            mapping["".join(check)] = 8
            reverse_mapping[8] = check
        elif len(check) == 5:
            if 7 in reverse_mapping and len([x for x in check if x in reverse_mapping[7]]) == 3:
                mapping["".join(check)] = 3
                reverse_mapping[3] = check
            elif 6 in reverse_mapping and len([x for x in check if x in reverse_mapping[6]]) == 5:
                mapping["".join(check)] = 5
                reverse_mapping[5] = check
            elif 6 in reverse_mapping and 7 in reverse_mapping:
                mapping["".join(check)] = 2
                reverse_mapping[2] = check
            else:
                digits.append(check)
        elif len(check) == 6:
            if 4 in reverse_mapping and len([x for x in check if x in reverse_mapping[4]]) == 4:
                mapping["".join(check)] = 9
                reverse_mapping[9] = check
            elif 4 in reverse_mapping and 7 in reverse_mapping and len([x for x in check if x in reverse_mapping[7]]) == 3:
                mapping["".join(check)] = 0
                reverse_mapping[0] = check
            elif 4 in reverse_mapping and 7 in reverse_mapping:
                mapping["".join(check)] = 6
                reverse_mapping[6] = check
            else:
                digits.append(check)
        else:
            print(check)
            exit()

    return int("".join([str(mapping["".join(sorted([*x]))]) for x in data[1]]))

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_digits_with_unique_number_of_segments(data)

    # Part 2
    solution2 = output_sum(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

