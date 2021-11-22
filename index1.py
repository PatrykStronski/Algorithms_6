import random
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
from generate_random_graph import create_random_graph
from statistics import mean
import time
import random

graph = csr_matrix(create_random_graph(100,5))

start = 0

d_times = []
bf_times = []

for _ in range(0,10):
    end = random.randint(1, 100)
    
    time_strt = time.time()
    shortest_path(graph, method='D', unweighted=False, indices=[start, end])
    d_time = 1000 * (time.time() - time_strt)
    d_times.append(d_time)
    print(f'Dijkstra: {d_time}ms')

    time_strt = time.time()
    shortest_path(graph, method='BF', unweighted=False, indices=[start, end])
    bf_time = 1000 * (time.time() - time_strt)
    bf_times.append(bf_time)
    print(f'Bellamn Ford: {bf_time}ms')

print(f'Mean search time for Dijkstra: {mean(d_times)}')
print(f'Mean search time for BF: {mean(bf_times)}')