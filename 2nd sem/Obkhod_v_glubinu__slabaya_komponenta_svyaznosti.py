def read_graph():
    N, M = map(int, input().split())
    G = {}
    for i in range(M):
        v1, v2 = input().split()
        for v in v1, v2:
            if v not in G:
                G[v] = []
        G[v1].append(v2)
    return G, N, M

def dfs(G, stack, used=None):
    if used is None:
        used = set()
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            dfs(G, v, used)
    stack.append(vertex)
    return stack


G, N, M = read_graph()
stack = []
print(dfs(G, stack))