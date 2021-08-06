
def read_graph():
    G = {}
    N, M = map(int, input().split())
    for i in range(M):
        v1, v2, ves = map(int, input().split())
        for v in v1, v2:
            if v not in G:
                G[v] = {}
        G[v1][v2] = ves
        G[v2][v1] = ves
    return N, G, v1

def Prima_2(G, v, N):
    tree = []
    tree_ves = 0
    pool = {}
    used = {v}
    for vertex in G.keys():
        pool[vertex] = (float('+inf'), (None, None))
    del pool[v]
    for _ in range(N - 1):
        for neig in G[v]:
            if neig not in used:
                if pool[neig][0] > G[v][neig]:
                    pool[neig] = (G[v][neig], (v, neig))
        min = float('+inf')
        min_ind = -1
        for i in pool.keys():
            if pool[i][0] < min:
                min_ind = i
                min = pool[i][0]
        v = min_ind
        tree_ves += min
        tree.append(pool[v][1])
        del pool[v]
        used.add(v)

    return tree, tree_ves

N, G, v = read_graph()
tree, tree_ves = Prima(G, v, N)
print(tree_ves)
for el in tree:
    print(*el)
