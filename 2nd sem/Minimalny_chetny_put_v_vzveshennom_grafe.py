import heapq

def read_graph(m):
    G = {}
    for i in range(m):
        v1, v2, ves = map(int, input().split())
        for v in v1, v2:
            if v not in G:
                G[v] = {}
        G[v1][v2] = G[v2][v1] = ves
    return G

def read_graph_chet_nechet(m):
    G = {}
    for i in range(m):
        v1, v2, ves = map(int, input().split())
        for v in v1, v2:
            if str(v) + '0' not in G:
                G[str(v) + '0'] = {}
                G[str(v) + '1'] = {}
        G[str(v1) + '0'][str(v2) + '1'] = ves
        G[str(v2) + '0'][str(v1) + '1'] = ves
        G[str(v1) + '1'][str(v2) + '0'] = ves
        G[str(v2) + '1'][str(v1) + '0'] = ves
    return G

def deikstra_2(G, start):
    start = str(start) + '0'
    heap = []
    distances = {v: float('+inf') for v in G}
    used = set()
    distances[start] = 0
    heapq.heappush(heap, (0, start))
    while len(heap) > 0:
        v = heapq.heappop(heap)[1]
        if v not in used:
            used.add(v)
            for neig in G[v]:
                tmp = distances[v] + G[v][neig]
                if distances[neig] > tmp:
                    heapq.heappush(heap, (tmp, neig))
                    distances[neig] = tmp
    return distances

def path_recovery(G, dist, end):
    path = [end]
    end = str(end) + '0'
    if dist[end] == float('inf'):
        return []
    k = dist[end]
    while k > 0:
        for v in G.keys():
            if v != end and v in G[end] and dist[v] == k - G[v][end]:
                path.append(v[:-1:])
                k -= G[v][end]
                end = v
                break
    return path[::-1]

n, m = map(int, input().split())
G = read_graph_chet_nechet(m)
k = int(input())
for _ in range(k):
    path = []
    start, end = map(int, input().split())
    dist = deikstra_2(G, start)
    path = path_recovery(G, dist, end)
    if path == []:
        print(-1)
    else:
        print(*path)