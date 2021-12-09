#!/usr/bin/env python3
import fileinput
import math

heights = [list(map(int, line.strip())) for line in fileinput.input()]
mx, my = len(heights[0]), len(heights)


def in_grid(point):
    y, x = point
    return 0 <= y < my and 0 <= x < mx


def adjacent(y, x):
    locations = filter(in_grid, [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)])
    return [(y1, x1, heights[y1][x1]) for y1, x1 in locations]


def part1():
    risk = 0

    for y in range(my):
        for x in range(mx):
            (ly, lx, low) = min(adjacent(y, x), key=lambda n: n[2])
            v = heights[y][x]
            if low > v:
                risk += v + 1
    return risk


def part2():
    visited = set()

    def visit(y, x):
        if (y, x) in visited:
            return 0

        visited.add((y, x))
        to_visit = filter(lambda p: p not in visited, adjacent(y, x))
        to_visit = [(y1, x1, v1) for y1, x1, v1 in to_visit if v1 < 9]
        v = heights[y][x]

        gt = [visit(y1, x1) for (y1, x1, v1) in to_visit if v1 > v]
        lt = [visit(y1, x1) for (y1, x1, v1) in to_visit if v1 < v]
        return 1 + sum(gt) + sum(lt)

    basins = []
    for y in range(my):
        for x in range(mx):
            if (y, x) in visited:
                continue
            elif heights[y][x] == 9:
                visited.add((y, x))
            else:
                v = visit(y, x)
                # print('basin from', (y, x), v)
                basins.append(v)

    basins.sort(reverse=True)
    return math.prod(basins[:3])


print(part1(), part2())
