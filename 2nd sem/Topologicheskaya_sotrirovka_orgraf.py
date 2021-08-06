def read_graph():
    N, M = map(int, input().split())
    G = {}
    for i in range(M):
        v1, v2 = map(int, input().split())
        for v in v1, v2:
            if v not in G:
                G[v] = []
        G[v1].append(v2)
    return G, N, M

def dfs(G, stack, vertex, stack1, used=None):
    zikl = []
    if used is None:
        used = set()
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            stack1.append(v)
            zikl = dfs(G, stack, v, stack1, used)
            if zikl != []:
                return zikl
            stack1.pop()
        else:
            if v in stack1:
                return stack1[stack1.index(v)::]
    stack.append(vertex)
    return []

def ifzikl(G, stack):
    used = set()
    for v in G.keys():
        if v not in used:
            stack1 = [v]
            zikl = dfs(G, stack, v, stack1, used)
            if zikl != []:
                return zikl
    return zikl

G, N, M = read_graph()
stack = []
zikl = ifzikl(G, stack)
if zikl != []:
    print('NO')
else:
    if len(stack) < N:
        for i in range(N):
            if i not in stack:
                stack.append(i)
    stack = stack[::-1]
    print(*stack)