from queue import Queue

def read_graph():
    N, M = map(int, input().split())
    G = {}
    for i in range(M):
        v1, v2 = input().split()
        for v in v1, v2:
            if v not in G:
                G[v] = []
        G[v1].append(v2)
        G[v2].append(v1)
    return G, N, M

def bfs(G, vertex, used, stack):
    q = Queue()
    q.put(vertex)
    while not q.empty():
        v = q.get()
        if v not in used:
            used.add(v)
            for neig in G[v]:
                if neig not in used:
                    q.put(neig)
            stack.append(v)
    return stack

G, N, M = read_graph()
used = set()
components = []
for v in G.keys():
    if v not in used:
        stack = []
        components.append(bfs(G, v, used, stack))
for i in range(1, N + 1): #только если вершины графа - цифры начиная с 1
    if str(i) not in used:
        components.append([str(i)])
print(*components)