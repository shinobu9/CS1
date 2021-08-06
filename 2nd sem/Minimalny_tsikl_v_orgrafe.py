from queue import Queue

def read_graph():
    N, M = map(int, input().split())
    G = {}
    for i in range(M):
        v1, v2 = input().split()
        vertex = v1
        for v in v1, v2:
            if v not in G:
                G[v] = set()
        G[v1].add(v2)
    return G, vertex

def bfs_path(G, start, loops):
    path = {v: None for v in G}
    q = Queue()
    q.put(start)
    path[start] = [start]
    while not q.empty():
        v = q.get()
        used.add(v)
        for neig in G[v]:
            if path[neig] is None:
                q.put(neig)
                path[neig] = path[v] + [neig]
            elif neig in path[v]:
                loops.append(path[v][path[v].index(neig)::])
    return []

G, vertex = read_graph()
loops = []
used = set()
for v in G.keys():
    if v not in used:
        bfs_path(G, v, loops)
min = float('+inf')
for el in loops:
    if len(el) < min and el != []:
        min = len(el)
        min_loop = el
if min == float('+inf'):
    print('NO CYCLES')
else:
    print(*min_loop)