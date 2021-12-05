#!/usr/bin/env python3
import collections
import fileinput
import itertools
import re


def points_between(pair):
    x1, y1, x2, y2 = pair
    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                yield x, y
    else:
        xd = 1 if x1 < x2 else -1
        yd = 1 if y1 < y2 else -1
        yield x1, y1
        x, y = x1, y1
        while x != x2:
            while y != y2:
                x += xd
                y += yd
                yield x, y


def read_input():
    input_re = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    for line in fileinput.input():
        yield tuple(map(int, input_re.match(line).groups()))


def solution(input):
    point_counter = collections.Counter(point for pair in input for point in points_between(pair))
    overlapping_counts = list(filter(lambda count: count > 1, point_counter.values()))
    return len(overlapping_counts)


part1_input, part2_input = itertools.tee(read_input(), 2)

part1 = solution(filter(lambda p: p[0] == p[2] or p[1] == p[3], part1_input))
part2 = solution(part2_input)

print(part1, part2)
