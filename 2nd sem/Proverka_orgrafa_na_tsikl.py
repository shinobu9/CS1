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

def dfs(G, vertex, used, stack):
    zikl = []
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            stack.append(v)
            zikl = dfs(G, v, used, stack)
            if zikl != []:
                return zikl
            stack.pop()
        else:
            if v in stack:
                return stack[stack.index(v)::]
    return []

def ifzikl(G):
    used = set()
    for v in G.keys():
        if v not in used:
            stack = [v]
            zikl = dfs(G, v, used, stack)
            if zikl != []:
                return zikl
    return zikl

def count_weak_connect(G):
    used = set()
    N = 0
    for vertex in G.keys():
        if vertex not in used:
            dfs(G, vertex, used)
            N += 1
    return N

G, N, M = read_graph()
zikl = ifzikl(G)
if zikl != []:
    print(*zikl)
else:
    print('YES')