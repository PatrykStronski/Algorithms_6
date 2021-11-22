from statistics import mean
import time
from generate_map import new_map
from find_path import generate_free_place

map = new_map()
print(map)


for _ in range(0,5):
    start = generate_free_place(map)
    end = generate_free_place(map)
    while start == end:
        end = generate_free_place(map)