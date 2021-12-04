#!/usr/bin/env python3
import itertools
import sys


class Cell:
    def __init__(self, n):
        self.n = n
        self.is_hit = False

    def hit(self):
        self.is_hit = True

    def __str__(self):
        if self.is_hit:
            return f'\033[1m{self.n:2}\033[0m'
        return f'{self.n:2}'

    def __repr__(self):
        return self.__str__()


class Line:
    def __init__(self, cells):
        self.cells = cells

    @property
    def is_hit(self):
        return all([cell.is_hit for cell in self.cells])

    def __str__(self):
        return f'{self.cells}'

    def __repr__(self):
        return self.__str__()


class Board:
    def __init__(self, cells):
        self.cells = cells
        self.value_to_cells = {c.n: c for c in self.cells}
        self.rows = [Line(cells[n:n + 5]) for n in range(0, 25, 5)]
        self.cols = [Line([cells[n] for n in range(k, 25, 5)]) for k in range(0, 5)]

    def render(self):
        for row in self.rows:
            print(row)

    def play(self, n):
        c = self.value_to_cells.get(n)
        if c:
            c.hit()

    @property
    def is_winner(self):
        return any([row.is_hit for row in self.rows]) or any([col.is_hit for col in self.cols])

    @property
    def unplayed_values(self):
        return [cell.n for cell in self.cells if not cell.is_hit]


def process_input():
    with sys.stdin as f:
        lines = f.readlines()
    numbers = [int(n) for n in lines[0].split(',')]
    boards_lines = [[Cell(int(n)) for n in l.strip().split(' ') if n]
                    for l in lines[1:]
                    if len(l) > 1]
    boards = [Board(list(itertools.chain(*boards_lines[i:i + 5])))
              for i in range(0, len(boards_lines), 5)]
    return numbers, boards


def part1():
    ns, bs = process_input()
    for n in ns:
        for b in bs:
            b.play(n)
            if b.is_winner:
                b.render()
                print('-----')
                print('first board to win', sum(b.unplayed_values) * n)
                return


def part2():
    last_n, last_board = None, None

    ns, bs = process_input()
    for n in ns:
        for b in bs:
            b.play(n)
        if not last_board and len([b for b in bs if b.is_winner]) == len(bs) - 1:
            last_board = [b for b in bs if not b.is_winner][0]
        if last_board and last_board.is_winner:
            last_n = n
            break

    last_board.render()
    print('-----')
    print('last board to win', sum(last_board.unplayed_values) * last_n)


# part1()
part2()
