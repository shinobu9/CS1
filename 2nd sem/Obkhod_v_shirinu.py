from queue import Queue

def read_graph(filename):
    N = M = None
    G = {}
    for line in open(filename, 'r'):
        if N is None:
            N, M = map(int, line.split())
            continue
        v1, v2 = line.split()
        for v in v1, v2:
            if v not in G:
                G[v] = []
        G[v1].append(v2)
        G[v2].append(v1)
    return G

def bfs(G, vertex, used=None):
    N = 0
    if used is None:
        used = set()
    q = Queue()
    q.put(vertex)
    while not q.empty():
        v = q.get()
        if v not in used:
            N += 1
            used.add(v)
            print('{} is {}-th vertex'.format(v, N))
            for neig in G[v]:
                if neig not in used:   # ускорение работы за счёт избегания повторов
                    q.put(neig)

G = read_graph()
used = set()
N = 0
for vertex in G.keys():
    if vertex not in used:
        bfs(G, vertex, used)
        N += 1