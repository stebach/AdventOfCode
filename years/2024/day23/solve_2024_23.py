"""
Solution for day 23 of year 2024
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = tuple(line.strip().split('-'))
    return line

def find_interconnected_starting_with_t(data):
    data_set = set(data)
    interconnected = 0
    computers = set()
    for connection in data:
        computers.add(connection[0])
        computers.add(connection[1])

    computers_list = list(computers)
    for computer1 in range(0, len(computers_list) - 2):
            for computer2 in range(computer1 + 1, len(computers_list) - 1):
                if (computers_list[computer1], computers_list[computer2]) in data_set or (computers_list[computer2], computers_list[computer1]) in data_set:
                    for computer3 in range(computer2 + 1, len(computers_list)):
                        if ((computers_list[computer1], computers_list[computer3]) in data_set or (computers_list[computer3], computers_list[computer1]) in data_set) \
                            and ((computers_list[computer2], computers_list[computer3]) in data_set or (computers_list[computer3], computers_list[computer2]) in data_set) \
                            and 't' in (computers_list[computer1][0], computers_list[computer2][0], computers_list[computer3][0]):
                            interconnected += 1

    return interconnected

def find_largest_set(data):
    computers = set()
    for connection in data:
        computers.add(connection[0])
        computers.add(connection[1])
    largest_set = set()
    data_set = set(data)

    counter = 0

    for computer in computers:
        counter += 1
        check = find_largest_set_recursive(data_set, [x for x in computers if x != computer], set([computer]))
        if len(check) > len(largest_set):
            largest_set = check
    return ",".join(sorted(list(largest_set)))

def find_largest_set_recursive(data, computers, current_set):
    largest_set = current_set
    for pos, computer in enumerate(computers):
        connected_to_all = True
        for connected in current_set:
            if (computer, connected) not in data and (connected, computer) not in data:
                connected_to_all = False
                break
        if connected_to_all:
            check = find_largest_set_recursive(data, computers[pos+1:], current_set | set([computer]))
            if len(check) > len(largest_set):
                largest_set = check

    return largest_set

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_interconnected_starting_with_t(data)

    # Part 2
    solution2 = find_largest_set(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
