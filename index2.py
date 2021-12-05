from statistics import mean
import time

from matplotlib.pyplot import draw
from generate_map import new_map, draw_map, draw_map_route
from find_path import generate_free_place
from find_path import a_star

map = new_map()

draw_map(map)
times = []

for _ in range(0,5):
    start = generate_free_place(map)
    end = generate_free_place(map)
    while start == end:
        end = generate_free_place(map)
    
    start_time = time.time()
    path = a_star(map, start, end)
    end_time = time.time()
    print(f'Calculated from {start} to {end}')
    times.append(end_time * 1000 - start_time * 1000)
    draw_map_route(map, path, start, end)

av = mean(times)
print(f'Average is: {av}')