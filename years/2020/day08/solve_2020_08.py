"""
Solution for day 08 of year 2020
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' ')
    return (line[0], int(line[1]))

def run_app(data, idx_nop_jmp_switch=-1):
    idx = 0
    seen = set()
    acc = 0
    loop = True

    while idx not in seen:
        seen.add(idx)
        if idx == len(data):
            loop = False
            break
        if (data[idx][0] == 'nop' and idx != idx_nop_jmp_switch) or (data[idx][0] == 'jmp' and idx == idx_nop_jmp_switch):
            idx += 1
        elif data[idx][0] == 'acc':
            acc += data[idx][1]
            idx += 1
        elif (data[idx][0] == 'jmp' and idx != idx_nop_jmp_switch) or (data[idx][0] == 'nop' and idx == idx_nop_jmp_switch):
            idx += data[idx][1]
        else:
            print(data[idx])
            exit()

    return (acc, loop)

def fix_app(data):
    index_to_check = [x[0] for x in enumerate(data) if x[1][0] in ['nop','jmp']]
    for idx in index_to_check:
        res = run_app(data, idx)
        if not res[1]:
            return res[0]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = run_app(data)[0]

    # Part 2
    solution2 = fix_app(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
