import sys
input = sys.stdin.readline

# sys.setrecursionlimit(200000)


def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))
def insr():
    s = input()
    return (list(s[:len(s) - 1]))
def invr():
    return (map(int, input().split()))


def solution():
    n, m, q = inlt()
    s = [0] + list(map(int, input()[:-1]))

    parent = [i for i in range(n + 2)]
    # union find
    # def find(x):
    #     if parent[x] != x:
    #         parent[x] = find(parent[x])
    #     return parent[x]
    # find without the iteration
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

    priority = []
    for _ in range(m):
        l, r = inlt()
        while find(l) <= r:
            l = find(l)
            priority.append(l)
            union(l, l+1)
    length = len(priority)

    priority_code = [n] * (n+1)
    for idx, x in enumerate(priority):
        priority_code[x] = idx + 1

    fenwick = [0] * (n+1)
    def lowbit(x):
        return x & -x
    def update(index, d):
        while index <= n:
            fenwick[index] += d
            index += lowbit(index)
    def getsum(index):
        res = 0
        while index > 0:
            res += fenwick[index]
            index -= lowbit(index)
        return res

    for i in range(1, n+1):
        if s[i] == 1:
            update(priority_code[i], 1)

    for i in range(q):
        x = inp()
        if s[x] == 0:
            update(priority_code[x], 1)
        else:
            update(priority_code[x], -1)
        s[x] ^= 1
        count = getsum(n)
        if count <= length:
            print(count - getsum(count))
        else:
            print(length - getsum(length))

    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
