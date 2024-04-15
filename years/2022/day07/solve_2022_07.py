"""
Solution for day 07 of year 2022
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())


def parse_lines(lines):
    sizes = {}
    tree = get_tree('/', lines, '', True)
    set_size(tree, sizes)
    return sizes

def set_size(tree, sizes):
    sub_size = 0
    if len(tree['sub']) > 0:
        for sub_tree in tree['sub']:
            set_size(sub_tree, sizes)
            sub_size += sub_tree['size']
    
    tree['size'] += sub_size
    sizes[tree['name']] = tree['size']

def get_tree(dir, lines, prefix, is_root=False, parent = None):
    current_dir = {
        'name' : prefix + dir,
        'size' : 0,
        'sub'  : []
    }
    if parent != None:
        parent['sub'].append(current_dir)
    while len(lines) > 0:
        line = lines.pop(0).strip()
        if (line[0:2] == '$ '):
            line = line[2:].split(' ')
            if line[0] == 'cd':
                if line[1] == '/':
                    if not is_root:
                        return True
                if line[1] == '..':
                    return False
                else:
                    if is_root:
                        check = get_tree('', lines, '', False, current_dir)
                    else:
                        check = get_tree('/' + line[1], lines, current_dir['name'], False, current_dir)
                    if check:
                        return check
            elif line[0] == 'ls':
                while len(lines) > 0 and lines[0][0] != '$':
                    info = lines.pop(0).split(' ')
                    if info[0] != 'dir':
                        current_dir['size'] += int(info[0])
            else:
                print(line)
                exit()
        else:
            print(line)
            exit()
    if is_root:
        return current_dir['sub'][0]


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([data[x] for x in list(data) if data[x] <= 100_000])

    # Part 2
    needed = 30000000 - (70000000 - data[''])
    solution2 = min([data[x] for x in list(data) if data[x] >= needed])
    
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

