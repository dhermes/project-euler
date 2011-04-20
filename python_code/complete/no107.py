from python_code.functions import get_data

data = [row.split(',') for row in get_data(107).split('\r\n') if row]

adjacency = {}
size = len(data)
network_sum = 0
# UNDIRECTED
for node in range(size - 1):
    for dest in range(node + 1, size):
        if data[node][dest] != '-':
            value = int(data[node][dest])
            network_sum += value
            if node in adjacency:
                adjacency[node].append((dest, value))
            else:
                adjacency[node] = [(dest, value)]
            if dest in adjacency:
                adjacency[dest].append((node, value))
            else:
                adjacency[dest] = [(node, value)]

# PRIMs ALGO
# arbitrarily start at vertex 0
vertices = [0]
edges = []
min_sum = 0
while set(vertices) != set(range(size)):
    # Find next edge
    candidates = {}
    for vertex in vertices:
        for node in adjacency[vertex]:
            if node[0] not in vertices:
                candidates[(vertex, node[0])] = node[1]
    new_edge, val = sorted(candidates.items(), key=lambda pair: pair[1])[0]
    min_sum += val
    edges.append(new_edge)
    vertices.append(new_edge[1])

print network_sum - min_sum
