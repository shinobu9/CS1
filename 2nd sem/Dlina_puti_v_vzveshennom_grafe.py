from queue import Queue
from random import randint
import heapq

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
                G[v] = {}
        G[v1][v2] = G[v2][v1] = randint(10, 99)
    return G

def deikstra_1(G, start):
    distances = {v: float('+inf') for v in G}
    q = Queue()
    q.put(start)
    distances[start] = 0
    while not q.empty():
        v = q.get()
        for neig in G[v]:
            tmp = distances[v] + G[v][neig]
            if distances[neig] > tmp:
                q.put(neig)
                distances[neig] = tmp
    return distances

def deikstra_2(G, start):
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

def Belman_Ford(N, Edges):
    d = [float('+inf') for _ in range(N)]
    d[0][start] = 0
    for i in range(N):
        for x, y in Edges:  #ребра
            d[y] = min(d[y], d[x] + w)

def Floyd_Y():
    G = ...
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

G = read_graph()
dist = deikstra_2(G, 'A')