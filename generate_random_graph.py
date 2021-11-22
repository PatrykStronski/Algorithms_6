import random

def create_row(node_number: int, max_weight: int) -> list:
    cons = []
    for ind in range(0, node_number):
        cons.append(random.randint(0, max_weight))
    return cons

def create_random_graph(node_number: int, max_weight: int) -> list:
    graph_matrix = []

    for n in range(0, node_number):
        connections = create_row(node_number, max_weight)
        graph_matrix.append(connections)

    return graph_matrix