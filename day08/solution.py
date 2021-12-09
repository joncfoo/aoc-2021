#!/usr/bin/env python3
import fileinput


class Entry:
    def __init__(self, digits, display):
        self.digits = sorted([set(d) for d in digits], key=len)
        self.display = display
        self.mapping = {1: self.digits[0], 7: self.digits[1], 4: self.digits[2], 8: self.digits[9]}

        for n in self.digits[6:9]:
            if len(self.mapping[8] - n - self.mapping[1]) == 0:
                self.mapping[6] = n
            elif len(n.symmetric_difference(self.mapping[8]) - self.mapping[4]) == 0:
                self.mapping[0] = n
            else:
                self.mapping[9] = n
        for n in self.digits[3:6]:
            if len(self.mapping[7] - n) == 0:
                self.mapping[3] = n
            elif len(self.mapping[9] - n) == 1:
                self.mapping[5] = n
            else:
                self.mapping[2] = n

    def value(self):
        output = []
        for n in self.display:
            for k, v in self.mapping.items():
                if v == set(n):
                    output.append(k)
        return output


part1 = 0
part2 = 0

for line in fileinput.input():
    entry = Entry(*[part.strip().split() for part in line.split('|')])
    value = entry.value()
    for v in value:
        if v in (1,4,7,8):
            part1 += 1
    part2 += 1000*value[0] + 100*value[1] + 10*value[2] + value[3]

print('part 1:', part1)
print('part 2:', part2)
