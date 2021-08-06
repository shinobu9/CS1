from queue import Queue

def chess_plate_for_horse():
    G = dict()
    for i in 'abcdefgh':
        for j in '12345678':
            G[i + j] = set()
    for x in G:
        for y in G:
            if abs((ord(x[0]) - ord(y[0])) * (ord(x[1]) - ord(y[1]))) == 2:
                G[x].add(y)
                G[y].add(x)
    return G

def horse(start, end):
    G = chess_plate_for_horse()
    start = start
    path = {v: None for v in G}
    q = Queue()
    q.put(start)
    path[start] = [start]
    while not q.empty():
        v = q.get()
        for neig in G[v]:
            if path[neig] is None:
                q.put(neig)
                path[neig] = path[v] + [neig]
                if neig == end:
                    return path[neig]
    return None

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
                G[v] = set()
        G[v1].add(v2)
        G[v2].add(v1)
    return G

def read_graph_chet_nechet(filename):
    N = M = None
    G = {}
    for line in open(filename, 'r'):
        if N is None:
            N, M = map(int, line.split())
            continue
        v1, v2 = line.split()
        for v in v1, v2:
            if v + '0' not in G:
                G[v + '0'] = set()
                G[v + '1'] = set()
        G[v1 + '0'].add(v2 + '1')
        G[v2 + '0'].add(v1 + '1')
        G[v1 + '1'].add(v2 + '0')
        G[v2 + '1'].add(v1 + '0')
    return G

def bfs_chet_path(G, start):
    start = start + '0'
    path = {v: None for v in G}
    q = Queue()
    q.put(start)
    path[start] = [start]
    while not q.empty():
        v = q.get()
        for neig in G[v]:
            if path[neig] is None:
                q.put(neig)
                path[neig] = path[v] + [neig]
    #res = {}
    #for i in path:
    #    if i[-1] == '0':
    #        res[i[:-1]]=[x[:1] for x in path[i]]
    return path

def bfs_dlina_puty(G, start):
    distances = {v: None for v in G}
    q = Queue()
    q.put(start)
    distances[start] = 0
    while not q.empty():
        v = q.get()
        for neig in G[v]:
            if distances[neig] is None:
                q.put(neig)
                distances[neig] = distances[v] + 1
    return distances

def path_slow(G, start, end):
    distances = bfsbfs_dlina_puty(G, start)
    res = [end]
    while distances[end] != 0:
        for v in G[end]:
            if distances[end] - distances[v] == 1:
                end = v
                res.append(end)
                break
    return res[::-1]

def bfs_path(G, start):
    path = {v: None for v in G}
    q = Queue()
    q.put(start)
    path[start] = [start]
    while not q.empty():
        v = q.get()
        for neig in G[v]:
            if path[neig] is None:
                q.put(neig)
                path[neig] = path[v] + [neig]
    return path

def bfs_zikl(G, start):
    parent = {v: None for v in G}
    q = Queue()
    q.put(start)
    parent[start] = None
    while not q.empty():
        v = q.get()
        for neig in G[v]:
            if parent[neig] is None:
                q.put(neig)
                parent[neig] = v
            elif parent[v] != neig:
                #мы нашли цикл
                pass
    return parent

G = chess_plate_for_horse()
print(G)

#G = read_graph()
#dist = bfs(G, '----')
#for v in G:
#    if v[-1] == '0':
#        print(v, dist[v])