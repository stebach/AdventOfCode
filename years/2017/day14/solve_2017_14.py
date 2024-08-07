"""
Solution for day 14 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def count_used(data):
    count = 0
    for i in range(128):
        count += bin(int(get_knot_hash(data + '-' + str(i)), 16))[2:].zfill(128).count('1')
    return count

def count_regions(data):
    grid = []
    for i in range(128):
        grid.append([int(x) for x in list(bin(int(get_knot_hash(data + '-' + str(i)), 16))[2:].zfill(128))])
    next_group = 2
    for row in range(128):
        for col in range(128):
            if grid[row][col] != 0:
                orig = grid[row][col]
                if col > 0 and grid[row][col - 1] > 0:
                    grid[row][col] = grid[row][col - 1]
                    orig = grid[row][col]
                if row > 0 and grid[row - 1][col] > 0:
                    grid[row][col] = grid[row - 1][col]
                    if orig != 1:
                        grid = [[orig if y == grid[row][col] else y for y in x] for x in grid]
                    orig = grid[row][col]
                if orig == 1:
                    grid[row][col] = next_group
                    next_group += 1
    result = set()
    [[result.add(x) for x in y if x > 0] for y in grid]
    return len(result)

def get_knot_hash(data):
    mylist = [ord(x) for x in list(data)] + [17, 31, 73, 47, 23]
    sparse_hash = get_hash(mylist, runs=64)
    dense_hash = []
    while len(dense_hash) < 16:
        dense_hash.append(
            sparse_hash[0 + 16 * len(dense_hash)] ^
            sparse_hash[1 + 16 * len(dense_hash)] ^
            sparse_hash[2 + 16 * len(dense_hash)] ^
            sparse_hash[3 + 16 * len(dense_hash)] ^
            sparse_hash[4 + 16 * len(dense_hash)] ^
            sparse_hash[5 + 16 * len(dense_hash)] ^
            sparse_hash[6 + 16 * len(dense_hash)] ^
            sparse_hash[7 + 16 * len(dense_hash)] ^
            sparse_hash[8 + 16 * len(dense_hash)] ^
            sparse_hash[9 + 16 * len(dense_hash)] ^
            sparse_hash[10 + 16 * len(dense_hash)] ^
            sparse_hash[11 + 16 * len(dense_hash)] ^
            sparse_hash[12 + 16 * len(dense_hash)] ^
            sparse_hash[13 + 16 * len(dense_hash)] ^
            sparse_hash[14 + 16 * len(dense_hash)] ^
            sparse_hash[15 + 16 * len(dense_hash)]
        )
    return "".join([('0' + hex(x)[2:])[-2:] for x in dense_hash])

def get_hash(lengths, size = 256, runs = 1):
    mylist = list(range(size))
    skips = 0
    moves = 0

    for run in range(runs):
        for length in lengths:
            mylist = mylist[0:length][::-1] + mylist[length:]
            toMove = (length + skips) % size
            mylist = mylist[toMove:] + mylist[0:toMove]
            moves = (moves + toMove) % size
            skips += 1
    mylist = mylist[-moves:] + mylist[0:-moves]
    return mylist

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_used(data)

    # Part 2
    solution2 = count_regions(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
