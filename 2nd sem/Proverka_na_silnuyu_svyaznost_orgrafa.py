def read_graph():
    N = int(input())
    M = int(input())
    G = {}
    G_inv = {}
    for i in range(M):
        v1, v2 = input().split()
        for v in v1, v2:
            if v not in G:
                G[v] = []
                G_inv[v] = []
        G[v1].append(v2)
        G_inv[v2].append(v1)

    return G, G_inv, N, M

def dfs(G, vertex, used, stack):
    used.add(vertex)
    for v in G[vertex]:
        if v not in used:
            dfs(G, v, used, stack)
    stack.append(vertex)

def strong_connection(G, G_inv):
    N = 0
    used = set()
    stack = []
    ALL_components = []
    for vertex in G.keys():
        if vertex not in used:
            dfs(G, vertex, used, stack)
    used = set()
    while len(stack) > 0:
        v = stack.pop()
        if v not in used:
            componenta = []
            dfs(G_inv, v, used, componenta)
            ALL_components.append(componenta)
            N += 1
    return N, ALL_components

G, G_inv, N, M = read_graph()
Num, ALL_components = strong_connection(G, G_inv)
if Num == 0:
    print('NO')
else:
    flag = 0
    for el in ALL_components:
        if len(el) == N:
            flag = 1
    if flag == 0:
        print('NO')
    else:
        print('YES')