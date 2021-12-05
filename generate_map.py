import random
import networkx as nx
import matplotlib.pyplot as plt

OBSTACLES = 40

def gen_new_obst(map: list) -> tuple:
    x = random.randint(0,9)
    y = random.randint(0,19)
    
    while map[x][y] == 'X':
        x = random.randint(0,9)
        y = random.randint(0,19)

    return (x,y)


def new_map() -> list:
    map = []
    for _ in range(0,10):
        map.append([0] * 20)
    
    for i in range(0,40):
        x, y = gen_new_obst(map)
        map[x][y] = 'X'
    
    return map

def draw_map(map: list):
    present_y = []
    present_x = []
    obstacles_y = []
    obstacles_x = []

    for col in range(0, 10):
        for row in range(0, 20):
            if map[col][row] == 'X':
                obstacles_x.append(row)
                obstacles_y.append(col)
            else:
                present_x.append(row)
                present_y.append(col)
    
    plt.scatter(present_x, present_y, s=150, c='blue')
    plt.scatter(obstacles_x, obstacles_y, s=150, c='black')
    plt.savefig(f'./figures/map.png')
    plt.show()
    
def draw_map_route(map: list, route: list, start: tuple, end: tuple, ind: int):
    present_y = []
    present_x = []
    obstacles_y = []
    obstacles_x = []

    for col in range(0, 10):
        for row in range(0, 20):
            if map[col][row] == 'X':
                obstacles_x.append(row)
                obstacles_y.append(col)
            else:
                present_x.append(row)
                present_y.append(col)

    way_x = [r for c, r in route]
    way_y = [c for c, r in route]

    plt.scatter(present_x, present_y, s=200, c='blue')
    plt.scatter(obstacles_x, obstacles_y, s=200, c='black')
    plt.scatter(way_x, way_y, s=200, c='green')
    plt.scatter([start[1], end[1]], [start[0], end[0]], s=200, c='yellow')
    plt.savefig(f'./figures/route{ind}.png')
    plt.show()
