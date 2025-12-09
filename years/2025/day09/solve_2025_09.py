"""
Solution for day 09 of year 2025
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([int(x) for x in line.strip().split(',')])

def largest_area(data, part2=False):
    sizes = []
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            dist = (abs(data[i][0] - data[j][0]) + 1) * (abs(data[i][1] - data[j][1]) + 1)
            sizes.append((dist, i, j, data[i], data[j]))
    sizes.sort(reverse=True)

    for size in sizes:
        if part2:
            if not inside_polygon(data, size[3], size[4]):
                continue
            return size[0]
        elif (size[3][0], size[4][1]) not in data and (size[4][0], size[3][1]) not in data:
            return size[0]


def point_on_edge(point, edge_point1, edge_point2):
    pointx, pointy = point
    edge1x, edge1y = edge_point1
    edge2x, edge2y = edge_point2

    if edge1y == edge2y == pointy and min(edge1x, edge2x) <= pointx <= max(edge1x, edge2x):
        return True
    if edge1x == edge2x == pointx and min(edge1y, edge2y) <= pointy <= max(edge1y, edge2y):
        return True
    return False

def point_in_polygon(polygon, point):
    x, y = point
    insideX = False
    insideY = False

    n = len(polygon)

    for i in range(n):
        polygon_point1 = polygon[i]
        polygon_point2 = polygon[(i + 1) % n]

        if point_on_edge(point, polygon_point1, polygon_point2):
            return True

        x1, y1 = polygon_point1
        x2, y2 = polygon_point2

        if x1 == x2:
            intersect = (y1 > y) != (y2 > y) and min(x1,x2) < x
            if intersect:
                insideX = not insideX
        else:
            intersect = (x1 > x) != (x2 > x) and min(y1,y2) < y
            if intersect:
                insideY = not insideY
    return insideX and insideY

def inside_polygon(polygon, point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    minx, maxx = sorted((x1, x2))
    miny, maxy = sorted((y1, y2))

    corners = [
        (minx, miny),
        (minx, maxy),
        (maxx, miny),
        (maxx, maxy)
    ]

    for corner in corners:
        if not point_in_polygon(polygon, corner):
            return False
    
    edges = [
        ((minx, miny), (minx, maxy)),
        ((maxx, miny), (maxx, maxy)),
        ((minx, miny), (maxx, miny)),
        ((minx, maxy), (maxx, maxy)),
    ]

    polygon_edge_count = len(polygon)
    polygon_edges = [(polygon[i], polygon[(i + 1) % polygon_edge_count]) for i in range(polygon_edge_count)]

    for edge1, edge2 in edges:
        for poly_edge1, poly_edge2 in polygon_edges:
            intersect = edges_intersect(edge1, edge2, poly_edge1, poly_edge2)

            if intersect:
                return False

    return True

def edges_intersect(edge1_point1, edge1_point2, edge2_point1, edge2_point2):
    x1, y1 = edge1_point1
    x2, y2 = edge1_point2
    x3, y3 = edge2_point1
    x4, y4 = edge2_point2

    if y1 == y2 and x3 == x4:
        minx1, maxx1 = sorted([x1, x2])
        miny2, maxy2 = sorted([y3, y4])
        return minx1 < x3 < maxx1 and miny2 < y1 < maxy2

    if x1 == x2 and y3 == y4:
        miny1, maxy1 = sorted([y1, y2])
        minx2, maxx2 = sorted([x3, x4])
        return miny1 < y3 < maxy1 and minx2 < x1 < maxx2

    return False

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = largest_area(data)

    # Part 2
    solution2 = largest_area(data, True)
    
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
