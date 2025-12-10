"""
Solution for day 10 of year 2025
"""

import os
import re
import z3

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    result = []
    line = line.strip()
    bracket_part = re.search(r"\[(.*?)\]", line).group(1)
    parentheses_parts = re.findall(r"\((.*?)\)", line)
    brace_part = re.search(r"\{(.*?)\}", line).group(1)

    result.append(int(bracket_part.replace('.', '0').replace('#', '1'), 2))

    lights_length = len(bracket_part)

    buttons = []
    for button in parentheses_parts:
        button_int = [int(toggle) for toggle in button.split(',')]
        buttons.append(int("".join(["1" if x in button_int else "0" for x in range(lights_length)]), 2))

    result.append(tuple(buttons))

    result.append([int(x) for x in brace_part.split(',')])

    return tuple(result)

def get_fewest_buttons(line):
    number_of_buttons = len(line[1])
    possible_combinations = 1 << number_of_buttons
    fewest_buttons = number_of_buttons + 1
    for combo in range(possible_combinations):
        lights = 0
        buttons_pressed = 0
        for button_index in range(number_of_buttons):
            if combo & (1 << button_index):
                lights ^= line[1][button_index]
                buttons_pressed += 1
                if buttons_pressed >= fewest_buttons:
                    break
        if lights == line[0]:
            if buttons_pressed < fewest_buttons:
                fewest_buttons = buttons_pressed
    return fewest_buttons

def try_buttons(sorted_buttons, current_joltage, target_joltage, current_button_index=0, debug = False):
    current_button_value = sorted_buttons[current_button_index]
    flipped = int(bin(current_button_value)[2:].rjust(len(target_joltage), '0') [::-1],2)

    button_connections = [i for i in range(flipped.bit_length()) if (flipped >> i) & 1]
    if (debug):
        print(f"{'  '*current_button_index}Trying button {current_button_index} value: {bin(current_button_value)} connections: {button_connections} current joltage: {current_joltage} target joltage: {target_joltage}")
    max_pushes = min([target_joltage[x] - current_joltage[x] for x in button_connections])
    spacing = "  " * current_button_index
    if debug:
        print(f"{spacing}Button {current_button_index}: {bin(current_button_value)} connections: {button_connections} max pushes: {max_pushes}")
    for pushes in range(max_pushes, -1, -1):
        new_joltage = current_joltage[:]
        for connection in button_connections:
            new_joltage[connection] += pushes

        if debug:
            print(f"{spacing}    Trying {pushes} pushes: New joltage: {new_joltage} from: {current_joltage}")
        if new_joltage == target_joltage:
            return (True, pushes)
        elif current_button_index + 1 < len(sorted_buttons):
            check = try_buttons(
                sorted_buttons,
                new_joltage,
                target_joltage,
                current_button_index + 1,
                debug
            )
            if check[0]:
                return (True, pushes + check[1])
    return (False,0)

def get_fewest_buttons_for_joltage_tooslow(line):
    sorted_buttons = tuple(sorted(line[1], key=lambda x: (x.bit_count(), x), reverse=True))


    debug = False
    if debug:

        print(f"Line: {bin(line[0])} Buttons: {[bin(b) for b in sorted_buttons]} Target joltage: {line[2]}")

    result = try_buttons(sorted_buttons, [0] * len(line[2]), line[2], 0, debug)
    
    return result[1]

def get_fewest_buttons_for_joltage(line):
    opt = z3.Optimize()
    pushes = z3.Int('pushes')
    counter = [z3.Int(f'counter_{i}') for i in range(len(line[1]))]

    buttons_map = [[] for _ in range(len(line[2]))];
    for button in range(len(line[1])):
        flipped = int(bin(line[1][button])[2:].rjust(len(line[2]), '0') [::-1],2)
        button_connections = [i for i in range(flipped.bit_length()) if (flipped >> i) & 1]
        for connection in button_connections:
            buttons_map[connection].append(button)


    for joltage_index in range(len(buttons_map)):
        opt.add(line[2][joltage_index] == sum([counter[x] for x in buttons_map[joltage_index]]))

    for c in counter:
        opt.add(c >= 0)

    opt.add(pushes == sum(counter))

    opt.minimize(pushes)

    opt.check()
    return int(str(opt.model()[pushes]))

def part1(data):
    total = 0
    for line in data:
        total += get_fewest_buttons(line)
    return total

def part2(data):
    total = 0
    for line in data:
        total += get_fewest_buttons_for_joltage(line)
    return total

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = part1(data)

    # Part 2
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

