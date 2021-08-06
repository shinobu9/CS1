def read_graph():
    N, M = map(int, input().split())
    G = {}
    for i in range(M):
        v1, v2 = input().split()
        for v in v1, v2:
            if v not in G:
                G[v] = []
        G[v1].append(v2)
        G[v2].append(v1)
    return G, N, M

def dvydolnost(G, vertex, black, white, used, last = 0):
    used.add(vertex)
    if last == 0:
        white.append(vertex)
    else:
        black.append(vertex)
    for neig in G[vertex]:
        if neig not in used:
            flag = dvydolnost(G, neig, black, white, used, (last + 1) % 2)
            if flag == 0:
                return 0
        elif last == 0 and neig in white:
            return 0
        elif last == 1 and neig in black:
            return 0
    return (black, white)

G, N, M = read_graph()
black = []
white = []
used = set()
for v in G.keys():
    if v not in used:
        flag = dvydolnost(G, v, black, white, used)
if flag == 0:
    print('Это не двудольный граф')
else:
    print('Первая доля: ', *black)
    print('Вторая доля: ', *white)