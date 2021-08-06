def dfs(u):
    vals = set()
    for v in a[u]:
        if d[v] == -1:
            dfs(v)
        vals.add(d[v])
    vals = sorted(vals)
    if vals[0] != 0:
        d[u] = 0
    else:
        for i in range(1, len(vals)):
            if vals[i] != vals[i - 1] + 1:
                d[u] = vals[i - 1] + 1
                break
        else:
            d[u] = vals[-1] + 1

n, m = map(int, imput().split())
a = {i: set() for i in range(n)}
for _ in range(m):
    u, v = map(int, input().split())
    a[u].add(v)
d = [-1] * n
d[0] = 0
dfs(n - 1)
print(d[::-1])