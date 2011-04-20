from python_code.functions import get_data

def astar(graph, size, minimum):
    start = (0, 0)
    target = (size - 1, size - 1)
    closed_nodes = {(0, 0): (None, graph[(0, 0)])}
    # node, parent, distance, don't store heuristic dist.
    open_nodes = {(1, 0): ((0, 0), graph[(0, 0)] + graph[(1, 0)]),
                  (0, 1): ((0, 0), graph[(0, 0)] + graph[(0, 1)])}
    def heuristic(node):
        return (2*size - 2 - sum(node))*minimum

    while target not in closed_nodes:
        min_val = None
        min_f = -1
        for node in open_nodes:
            val = open_nodes[node][1] + heuristic(node)
            if min_val is None:
                min_val = val
                min_f = node
            else:
                if val < min_val:
                    min_val = val
                    min_f = node

        closed_nodes[min_f] = open_nodes.pop(min_f)

        min_val = min_val - heuristic(min_f)
        node_x, node_y = min_f
        adjacent = [(node_x + 1, node_y), (node_x - 1, node_y),
                    (node_x, node_y + 1), (node_x, node_y - 1)]
        adjacent = [pair for pair in adjacent
                    if pair not in closed_nodes and pair in graph]
        for node in adjacent:
            if node in open_nodes:
                comp_val = open_nodes[node][1]
                new_val = min_val + graph[node]
                if new_val < comp_val:
                    open_nodes[node] = (min_f, new_val)
            else:
                open_nodes[node] = (min_f, min_val + graph[node])

    return closed_nodes[target][1]

data = [[int(entry) for entry in row.split(",")]
        for row in get_data(83).split("\n") if row]

arranged_data = {}
size = len(data)
for i in range(size):
    for j in range(size):
        arranged_data[(i, j)] = data[i][j]

minimum = min(arranged_data.values())
print astar(arranged_data, size, minimum)
