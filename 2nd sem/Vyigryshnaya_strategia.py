def read_graph():
    N, M = map(int, input().split())
    G = {i:[] for i in range(N)}
    for _ in range(M):
        x, y = map(int, input().split())
        G[x].append(y)

def dfs(G, x , res):
    for v in G[x]:
        if rex[v] == '':
            dfs(G, v, res)
        if res[v] == 'L':
            res[x] = 'W'
            break
    else:
        res[x] = 'L'

G = read_graph()
res = ['' for i in range(len(G))]
res[-1] = 'L'
dfs(G, 0, res)
print(res)