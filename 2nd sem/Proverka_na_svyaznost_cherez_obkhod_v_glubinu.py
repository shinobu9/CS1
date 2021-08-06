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

def dfs(G, vertex, used, stack):
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            dfs(G, v, used, stack)
    stack.append(vertex)
    return stack

G, N, M = read_graph()
used = set()
components = []
for v in G.keys():
    if v not in used:
        stack = []
        components.append(dfs(G, v, used, stack))
for i in range(1, N + 1): #только если вершины графа - цифры начиная с 1
    if str(i) not in used:
        components.append([str(i)])
print(*components)