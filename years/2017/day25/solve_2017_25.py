"""
Solution for day 25 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {
        'begin': lines[0].split(' ')[3][0],
        'checksum_after': int(lines[1].split(' ')[5]),
        'states': {}
    }
    lines = lines[3:]
    current_state = ''
    current_value = -1
    while len(lines) > 0:
        line = lines.pop(0)
        if (len(line.strip()) == 0):
            continue
        if line[0:9] == 'In state ':
            current_state = line[9]
            result['states'][current_state] = {}
        elif line[0:26] == '  If the current value is ':
            result['states'][current_state][int(line[26])] = [
                int(lines.pop(0).split(' ')[8][0]),
                1 if lines.pop(0).split(' ')[10].strip()[:-1] == 'right' else -1,
                lines.pop(0).split(' ')[8].strip()[:-1]
            ]
        else:
            print("what to do with this line?")
            print(line)
            exit()

    return result

def get_checksum(data):
    state = data['begin']

    tape = {}
    pos = 0
    for i in range(data['checksum_after']):
        task = data['states'][state][tape[pos] if pos in tape else 0]
        if task[0] == 0 and pos in tape:
            del tape[pos]
        elif task[0] == 1:
            tape[pos] = task[0]
        pos += task[1]
        state = task[2]

    return len(tape)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_checksum(data)

    # Part 2
    solution2 = None

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

