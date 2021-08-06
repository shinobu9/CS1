def read_graph(filename):
    N = M = None
    G = {}
    G_inv = {}
    for line in open(filename, 'r'):
        if N is None:
            N, M = map(int, line.split())
            continue
        v1, v2 = line.split()
        for v in v1, v2:
            if v not in G:
                G[v] = []
                G_inv[v] = []
        G[v1].append(v2)
        G_inv[v2].append(v1)

    return G, G_inv

def dfs(G, vertex, used, stack):
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            dfs(G, v, used)
    stack.append(vertex)

def strong_connection(G, G_inv):
    used = set()
    stack = []
    ALL_componennts = []
    for vertex in G.keys():
        if vertex not in used:
            dfs(G, vertex, used, stack)
    used = set()
    while len(stack) > 0:
        v = stack.pop()
        if v not in used:
            componenta = []
            dfs(G_inv, v, used, componenta)
            ALL_componennts.append(componenta)
            N += 1
    return N, ALL_componennts

G, G_inv = read_graph()
