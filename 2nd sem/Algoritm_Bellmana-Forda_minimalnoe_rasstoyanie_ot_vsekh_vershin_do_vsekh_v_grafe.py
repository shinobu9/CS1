from queue import Queue
from random import randint
import heapq

def read_graph(m):
    G = {}
    edges = []
    for i in range(m):
        v1, v2, ves = map(int, input().split())
        for v in v1, v2:
            if v not in G:
                G[v] = {}
        G[v1][v2] = ves
        edges.append([v1, v2])
    return G, edges

def Belman_Ford(N, G, edges):
    d = [float('+inf') for _ in range(N)]
    d[start] = 0
    for i in range(N):
        for x, y in edges:
            d[y] = min(d[y], d[x] + G[x][y])
    return d

n, m, start = map(int, input().split())
G, edges = read_graph(m)
dist = Belman_Ford(n, G, edges)
d = dist[:]
for x, y in edges:
    d[y] = min(d[y], d[x] + G[x][y])
for x, y in edges:
    d[y] = min(d[y], d[x] + G[x][y])
for i in range(n):
    if d[i] != dist[i]:
        dist[i] = float('+inf')
for el in dist:
    if el == float('+inf'):
        print('UDF', end=' ')
    else:
        print(el, end=' ')