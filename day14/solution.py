#!/usr/bin/env python3
import collections
import fileinput
import itertools

rules = {}
pair_count = collections.Counter()
letter_count = collections.Counter()

for line in fileinput.input():
    line = line.strip()
    if len(pair_count) == 0:
        pair_count.update(''.join(pair) for pair in itertools.pairwise(line))
        letter_count.update(line)
        continue
    elif len(line):
        pair, element = line.split(" -> ")
        rules[pair] = element


def expand():
    next_pair_count = collections.Counter()
    for pair in pair_count.keys():
        new_a = pair[0] + rules[pair]
        new_b = rules[pair] + pair[1]
        next_pair_count[new_a] += pair_count[pair]
        next_pair_count[new_b] += pair_count[pair]
        letter_count[rules[pair]] += pair_count[pair]
    return next_pair_count


for _ in range(40):
    pair_count = expand()

elements = letter_count.most_common()
print(elements[0][1] - elements[-1][1])
