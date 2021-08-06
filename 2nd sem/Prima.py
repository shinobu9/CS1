heap = []
def push(val):
    heap.append(val)
    val[1] = len(heap) - 1
    shift_up(len(heap) - 1)

def pop():
    a = heap[0]
    heap[0] = heap[-1]
    heap[0][1] = 0
    heap.pop()
    if not empty():
        shift_down(0)
    return(a)

def empty():
    return len(heap) == 0

def shift_up(id):
    if id == 0:
        return
    parent = (id - 1) // 2
    if heap[parent][0] > heap[id][0]:
        heap[parent], heap[id] = heap[id], heap[parent]
        heap[parent][1], heap[id][1] = heap[id][1], heap[parent][1]
        shift_up(parent)

def shift_down(id):
    nxt = heap[i][0]
    if id * 2 + 1 < len(heap):
        nxt = min(nxt, heap[2*id + 1][0])
    if id * 2 + 2 < len(heap):
        nxt = min(nxt, heap[2*id + 2][0])
    if heap[id][0] == nxt:
        return
    if heap [2*id + 1][0] == nxt:
        next_id = 2*id + 1
        heap[next_id], heap[id] = heap[id], heap[next_id]
        heap[next_id][1], heap[id][1] = heap[id][1], heap[next_id][1]
        shift_down(next_id)
        return
    next_id = 2*id + 2
    heap[next_id], heap[id] = heap[id], heap[next_id]
    heap[next_id][1], heap[id][1] = heap[id][1], heap[next_id][1]
    shift_down(next_id)

def read_graph():
    N, M = map(int, input().split())
    G = {}
    for _ in range(M):
        v1, v2, w = input().split()
        if v1 not in G:
            G[v1] = {}
        if v2 not in G:
            G[v2] = {}
        G[v1][v2] = float(w)
        G[v2][v1] = float(w)
    return G

def prim(G):
    start = next(iter(G.keys()))
    Vertexes = {x: [float('+inf'), i, None, x] for i, x in enumerate(G.keys())}
    Vertexes[start][0] = float('-inf')
    for v in G[start]:
        Vertexes[v][0] = G[start][v]
        Vertexes[v][2] = start

    for k, w in Vertexes.items():
        push(w)
    pop()
    res = []
    weight = 0
    used = {start}
    for _ in range(len(G) - 1):
        v = pop()
        res.append((v[2], v[3]))
        weight += v[0]
        used.add(v[3])
        for n in G[v[3]]:
            if n not in used:
                if G[v[3]][n] < Vertexes[n][0]:
                    Vertexes[n][0] = G[v[3]][n]
                    Vertexes[n][2] = v[3]
                    shift_up(Vertexes[n][1])
    return res, weight

G = read_graph()
min_tree, weight = prim(G)
print(min_tree, weight)