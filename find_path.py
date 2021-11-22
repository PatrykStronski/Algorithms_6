import random

def generate_free_number(map: list):
    x = random.randint(0,9)
    y = random.randint(0,19)
    
    while map[x][y] == 'X':
        x = random.randint(0,9)
        y = random.randint(0,19)

    return (x,y)

