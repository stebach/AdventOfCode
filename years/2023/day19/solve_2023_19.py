"""
Solution for day 19 of year 2023
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    rules = {}
    parts = []
    for line in lines:
        line_rules = []
        line = line.strip()
        if len(line) == 0:
            break
        for rule in line[line.index('{')+1:-1].split(','):
            match = regex.search(r'^([a-z]+)([<>])([0-9]+):([a-zA-Z]+)$',rule)
            if match:
                line_rules.append((match.group(1), match.group(2), int(match.group(3)), match.group(4)))
            else:
                line_rules.append((rule,))
        rules[line[:line.index('{')]] = tuple(line_rules)

    for line in lines:
        line = line.strip()
        if len(line) > 0 and line[0] == '{':
            match = regex.search(r'^{x=([0-9]+),m=([0-9]+),a=([0-9]+),s=([0-9]+)}$',line)
            parts.append((int(match.group(1)),int(match.group(2)),int(match.group(3)),int(match.group(4))))

    return (rules, tuple(parts))

def part1(data):
    """Solve part 1"""
    total = 0
    for part in data[1]:
        name = 'in'
        while name not in ('A','R'):
            for rule in data[0][name]:
                if len(rule) == 1:
                    name = rule[0]
                    break
                if (rule[1] == '>' and part['xmas'.index(rule[0])] > rule[2]) or (rule[1] == '<' and part['xmas'.index(rule[0])] < rule[2]):
                    name = rule[3]
                    break
        if name == 'A':
            total += sum(part)
    return total

def part2(data):
    """Solve part 2"""
    ranges = [
        (
            'in',
            (
                (1,4000),
                (1,4000),
                (1,4000),
                (1,4000),
            )
        )
    ]

    finished = []
    while len(ranges) > 0:
        check = ranges.pop()
        if check[0] in ('A','R'):
            finished.append(check)
        else:
            for rule in data[0][check[0]]:
                if len(rule) == 1:
                    ranges.append((rule[0], check[1]))
                else:
                    if rule[1] == '<' and check[1]['xmas'.index(rule[0])][0] < rule[2]:
                        copy = [(check[1][0][0],check[1][0][1]), (check[1][1][0],check[1][1][1]), (check[1][2][0],check[1][2][1]), (check[1][3][0],check[1][3][1])]
                        copy['xmas'.index(rule[0])] = (copy['xmas'.index(rule[0])][0], rule[2] - 1)
                        ranges.append((rule[3], tuple(copy)))

                        copy = [(check[1][0][0],check[1][0][1]), (check[1][1][0],check[1][1][1]), (check[1][2][0],check[1][2][1]), (check[1][3][0],check[1][3][1])]
                        copy['xmas'.index(rule[0])] = (rule[2], copy['xmas'.index(rule[0])][1])
                        check = (check[0], tuple(copy))

                    elif rule[1] == '>' and check[1]['xmas'.index(rule[0])][1] > rule[2]:
                        copy = [(check[1][0][0],check[1][0][1]), (check[1][1][0],check[1][1][1]), (check[1][2][0],check[1][2][1]), (check[1][3][0],check[1][3][1])]
                        copy['xmas'.index(rule[0])] = (rule[2] + 1, copy['xmas'.index(rule[0])][1])
                        ranges.append((rule[3], tuple(copy)))

                        copy = [(check[1][0][0],check[1][0][1]), (check[1][1][0],check[1][1][1]), (check[1][2][0],check[1][2][1]), (check[1][3][0],check[1][3][1])]
                        copy['xmas'.index(rule[0])] = (copy['xmas'.index(rule[0])][0], rule[2])
                        check = (check[0], tuple(copy))


    return sum([(x[1][0][1] - x[1][0][0] + 1) * (x[1][1][1] - x[1][1][0] + 1) * (x[1][2][1] - x[1][2][0] + 1) * (x[1][3][1] - x[1][3][0] + 1) for x in finished if x[0] == 'A'])

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
