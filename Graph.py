def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def find_path(graph, start, end, path=[]):
    path += [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

def edges_to_graph(edges):
    graph = dict()
    for edge in edges:
        node1 = edge.pop()
        if node1 not in graph:
            add_node(graph, node1)
        if edge:
            node2 = edge.pop()
            if node2 not in graph:
                add_node(graph, node2)
        else:
            node2 = node1
        graph[node1].append(node2)
    return graph


def add_edge(graph, edge):
    edge = set(edge)
    node1 = edge.pop()
    if edge:
        # not a loop
        node2 = edge.pop()
    else:
        # a loop
        node2 = node1
    if node1 in graph:
        graph[node1].append(node2)
    else:
        graph[node1] = [node2]


def add_node(graph, node):
    if node not in graph:
        graph[node] = []


def get_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            if {neighbour, node} not in edges:
                edges.append({node, neighbour})
    return edges


def get_neighbours(graph, node):
    nodes = []
    if node in graph:
        for neighbour in graph[node]:
            if neighbour not in nodes:
                nodes.append(neighbour)
    return nodes


def to_string(graph):
    res = "Nodes : "
    for k in graph:
        res += str(k) + " "
    res += "\nEdges : "
    for edge in get_edges(graph):
        res += str(edge) + " "
    return res


G = {'A': ['B', 'C'],
     'B': ['C', 'D'],
     'C': ['D'],
     'D': ['C'],
     'E': ['F'],
     'F': ['C']}

E = [['A', 'B'],
     ['A', 'C'],
     ['B', 'C'],
     ['B', 'D'],
     ['C', 'D'],
     ['E', 'F'],
     ['F', 'C']]

print(find_path(G, 'A', 'D'))
print(find_shortest_path(G, 'A', 'D'))
print(get_neighbours(G, 'A'))
print(to_string(G))

add_edge(G, {'E', 'A'})
add_node(G, 'X')
print(to_string(G))

A = edges_to_graph(E)
print(to_string(A))