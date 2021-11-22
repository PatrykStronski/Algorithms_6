from statistics import mean
import time
from generate_map import new_map
from find_path import generate_free_place
from find_path import a_star

map = new_map()

for r in map:
    print(r)

times = []

for _ in range(0,5):
    start = generate_free_place(map)
    end = generate_free_place(map)
    while start == end:
        end = generate_free_place(map)
    
    start_time = time.time()
    list = a_star(map, start, end)
    end_time = time.time()
    print(f'Calculated from {start} to {end}')
    for p in list:
        print(p)
    times.append(end_time * 1000 - start_time * 1000)

av = mean(times)
print(f'Average is: {av}')