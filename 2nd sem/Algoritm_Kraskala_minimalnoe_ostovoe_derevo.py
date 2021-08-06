vertex_sets = {}

def make_set(x):
    return {'parent': x, 'count': 1}

def find_set(x):
    if vertex_sets[x]['parent'] == x:
        return x
    else:
        y = find_set(vertex_sets[x]['parent'])
        vertex_sets[x]['parent'] = y
        return y

def union_set(x, y):
    x, y = map(find_set, (x, y))
    if vertex_sets[x]['count'] < vertex_sets[y]['count']:
        x, y = y, x
    vertex_sets[y]['parent'] = x
    vertex_sets[x]['count'] += vertex_sets[y]['count']

def key_el(x):
    return x[2]

E = []
N, M = map(int, input().split())
for _ in range(M):
    x, y, w = input().split()
    w = float(w)
    vertex_sets[x] = make_set(x)
    vertex_sets[y] = make_set(y)
    E.append((x, y, w))

E.sort(key=key_el)

min_tree = []
min_weight = 0
for x, y, w in E:
    if find_set(x) != find_set(y):
        min_weight += w
        min_tree.append((x, y, w))
        union_set(x, y)

print(min_weight, *min_tree, vertex_sets)