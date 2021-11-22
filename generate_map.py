import random

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