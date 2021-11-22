import random

def generate_edges(graph_matrix: list, node_number: int, max_weight: int):
    for _ in range(0,500):
        v1 = random.randint(0, node_number-1)
        v2 = random.randint(0, node_number-1)
        w = random.randint(0, max_weight)
        graph_matrix[v1][v2] = w
        graph_matrix[v2][v1] = w

def create_random_graph(node_number: int, max_weight: int) -> list:
    graph_matrix = []

    for n in range(0, node_number):
        connections = [0] * node_number
        graph_matrix.append(connections)

    generate_edges(graph_matrix, node_number, max_weight)

    return graph_matrix