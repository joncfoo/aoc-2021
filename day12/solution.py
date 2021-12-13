#!/usr/bin/env python3
import fileinput
from collections import defaultdict

edges = defaultdict(list)
for line in fileinput.input():
    a, b = line.strip().split("-")
    edges[a].append(b)
    edges[b].append(a)


def part1(node, seen):
    if node == 'end':
        return 1
    elif node.islower() and node in seen:
        return 0
    return sum([part1(n, seen | {node}) for n in edges[node]])


def part2(node, seen, twice=None):
    if node == 'end':
        return 1
    elif node == 'start' and seen:
        return 0
    elif node.islower() and node in seen:
        if twice:
            return 0
        twice = node
    return sum([part2(n, seen | {node}, twice) for n in edges[node]])


print(part1('start', set()))
print(part2('start', set()))
