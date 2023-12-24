"""
Solution for day 24 of year 2023
"""

import os
import sympy
import z3

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([tuple([int(y) for y in x.split(', ')]) for x in line.strip().split(' @ ')])

def find_intersection(data1, data2, mode_2d = False):
    point1 = data1[0]
    vector1 = data1[1]
    point2 = data2[0]
    vector2 = data2[1]

    t, u = sympy.symbols('t u')

    eq1 = sympy.Eq(point1[0] + t * vector1[0], point2[0] + u * vector2[0])
    eq2 = sympy.Eq(point1[1] + t * vector1[1], point2[1] + u * vector2[1])
    eq3 = sympy.Eq(point1[2] + t * vector1[2], point2[2] + u * vector2[2])

    if mode_2d:
        solution = sympy.solve((eq1, eq2), (t, u))
    else:
        solution = sympy.solve((eq1, eq2, eq3), (t, u))

    if solution:
        if solution[t] < 0 or solution[u] < 0:
            return None
        return (
            float(point1[0] + solution[t] * vector1[0]),
            float(point1[1] + solution[t] * vector1[1]),
            float(point1[2] if mode_2d else point1[2] + solution[t] * vector1[2])
        )
    else:
        return None

    return None

def part1(data, min_pos=200000000000000, max_pos=400000000000000):
    """Solve part 1"""
    count = 0
    for x in range(len(data)-1):
        print(x)
        for y in range(x+1, len(data)):
            z = find_intersection(data[x], data[y], True)
            if z is None:
                continue
            if z[0] >= min_pos and z[0] <= max_pos and z[1] >= min_pos and z[1] <= max_pos:
                count += 1
    return count

def part2(data):
    """Solve part 2"""

    point = [z3.Real(f'point_1'),z3.Real(f'point_2'),z3.Real(f'point_3')]
    vector = [z3.Real(f'vector_1'),z3.Real(f'vector_2'),z3.Real(f'vector_3')]
    solver = z3.Solver()
    for i in range(len(data)):
        time = z3.Real(f'time_{i}')
        other_point, other_vector = data[i]
        for x in range(3):
            solver.add(point[x] + time*vector[x] == other_point[x] + time*other_vector[x])
    solver.check()
    model = solver.model()
    return sum([int(str(model.evaluate(point[x]))) for x in range(3)])

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
