

n = 1 << 20
parent = [i for i in range(n)]

def find(x):
    x_copy = x
    while x != parent[x]:
        x = parent[x]
    while x_copy != x:
        parent[x_copy], x_copy = x, parent[x_copy]
    return x


def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[a] = b