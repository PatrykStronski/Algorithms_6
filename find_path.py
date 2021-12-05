import random

class Cell:
    x = 0
    y = 0
    g = 0
    h = 0
    f = 0
    parent = None

    def __init__(self, col: int, row: int, parent = None):
        self.col = col
        self.row = row
        self.parent = parent

    def calculate_remoteness(self, start: tuple, end: tuple):
        self.g = abs(self.col - start[0]) + abs(self.row - start[1])
        self.h = abs(self.col - end[0]) + abs(self.row - end[1])
        self.f = self.g + self.h

    def gen_possible_adjacent(self) -> list:
        points = []
        points.append((self.col-1, self.row))
        points.append((self.col-1, self.row+1))
        points.append((self.col, self.row+1))
        points.append((self.col+1, self.row+1))
        points.append((self.col+1, self.row))
        points.append((self.col+1, self.row-1))
        points.append((self.col, self.row-1))
        points.append((self.col-1, self.row-1))
        return points
    
    def find_adjacent(self, map: list, closed: list, start: tuple, end: tuple) -> list:
        possible_adjacent = self.gen_possible_adjacent()
        points = []
        for pos in possible_adjacent:
            if pos[0] >= 0 and pos[1] >= 0 and pos[0] < 10 and pos[1] < 20:
                if map[pos[0]][pos[1]] != 'X':
                    is_closed = list(filter(lambda el: el.col == pos[0] and el.row == pos[1], closed))
                    if len(is_closed) == 0:
                       p = Cell(pos[0], pos[1], self)
                       p.calculate_remoteness(start, end)
                       points.append(p)
        return points

def generate_free_place(map: list):
    x = random.randint(0,9)
    y = random.randint(0,19)
    
    while map[x][y] == 'X':
        x = random.randint(0,9)
        y = random.randint(0,19)

    return (y,x)

def find_lowest_fscore(points: list, strt: tuple, end: tuple) -> tuple:
    lowest = points[0]
    i = -1
    ind = 0
    for point in points:
        i += 1
        point.calculate_remoteness(strt, end)
        if lowest.f < point.f:
            lowest = point
            ind = i
    return (lowest, ind)

def insert_list(open_list: list, adjacents: list) -> list:
    for a in adjacents:
        existing = list(filter(lambda p: p.col == a.col and p.row == a.row, open_list))
        if len(existing) == 0:
            open_list.append(a)
        else:
            if(existing[0].g > a.g):
                existing[0].col = a.col
                existing[0].row = a.row
                existing[0].g = a.g
                existing[0].h = a.h
                existing[0].f = a.f
    return open_list

def a_star(map: list, strt: tuple, end: tuple) -> list:
    open_list = []
    closed_list = []

    open_list.append(Cell(strt[0], strt[1]))

    while len(open_list) > 0:
        lowest, ind = find_lowest_fscore(open_list, strt, end)
        if lowest.col == end[0] and lowest.row == end[1]:
            path = []
            current = lowest
            while current is not None:
                path.append((current.col, current.row))
                current = current.parent
            return path[::-1]
        closed_list.append(lowest)
        del open_list[ind]
        adjacents = lowest.find_adjacent(map, closed_list, strt, end)
        open_list = insert_list(open_list, adjacents)

    return []