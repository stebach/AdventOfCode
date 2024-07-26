"""
Solution for day 10 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()[0].split(',')))

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

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    hash = get_hash(list(data))
    solution1 = hash[0] * hash[1]

    # Part 2
    solution2 = get_knot_hash(','.join([str(x) for x in data]))
    print(solution2)
    exit()
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
