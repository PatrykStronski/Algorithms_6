import random

class Cell:
    vert = 0
    hor = 0
    g = 0
    h = 0
    f = 0
    parent = None

    def __init__(self, vert: int, hor: int, parent = None):
        self.vert = vert
        self.hor = hor
        self.parent = parent

    def calculate_remoteness(self, start: tuple, end: tuple):
        self.g = abs(self.vert - start[0]) + abs(self.hor - start[1])
        self.h = abs(self.vert - end[0]) + abs(self.hor - end[1])
        self.f = self.h + self.g

    def gen_possible_adjacent(self) -> list:
        points = []
        points.append((self.vert-1, self.hor))
        points.append((self.vert-1, self.hor+1))
        points.append((self.vert, self.hor+1))
        points.append((self.vert+1, self.hor+1))
        points.append((self.vert+1, self.hor))
        points.append((self.vert+1, self.hor-1))
        points.append((self.vert, self.hor-1))
        points.append((self.vert-1, self.hor-1))
        return points
    
    def find_adjacent(self, map: list, closed: list, start: tuple, end: tuple) -> list:
        possible_adjacent = self.gen_possible_adjacent()
        points = []
        for pos in possible_adjacent:
            if pos[0] >= 0 and pos[1] >= 0 and pos[0] < 10 and pos[1] < 20:
                if map[pos[0]][pos[1]] != 'X':
                    is_closed = list(filter(lambda el: el.vert == pos[0] and el.hor == pos[1], closed))
                    if len(is_closed) == 0:
                       p = Cell(pos[0], pos[1], self)
                       p.calculate_remoteness(start, end)
                       points.append(p)
        return points

def generate_free_place(map: list):
    vert = random.randint(0,9)
    hor = random.randint(0,19)
    
    while map[vert][hor] == 'X':
        vert = random.randint(0,9)
        hor = random.randint(0,19)

    return (vert,hor)

def find_lowest_fscore(points: list, strt: tuple, end: tuple) -> tuple:
    lowest = points[0]
    i = -1
    ind = 0
    for point in points:
        i += 1
        point.calculate_remoteness(strt, end)
        if lowest.f > point.f:
            lowest = point
            ind = i
    return (lowest, ind)

def insert_list(open_list: list, adjacents: list) -> list:
    for a in adjacents:
        existing = list(filter(lambda p: p.vert == a.vert and p.hor == a.hor, open_list))
        if len(existing) == 0:
            open_list.append(a)
        else:
            if(existing[0].g > a.g):
                existing[0].vert = a.vert
                existing[0].hor = a.hor
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
        if lowest.vert == end[0] and lowest.hor == end[1]:
            path = []
            current = lowest
            while current is not None:
                path.append((current.vert, current.hor))
                current = current.parent
            return path[::-1]
        closed_list.append(lowest)
        del open_list[ind]
        adjacents = lowest.find_adjacent(map, closed_list, strt, end)
        open_list = insert_list(open_list, adjacents)

    return []