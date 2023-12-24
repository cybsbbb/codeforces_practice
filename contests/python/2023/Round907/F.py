import sys

input = sys.stdin.readline


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
    q = inp()
    fenwick = [0] * (q + 10)

    def lowbit(x):
        return x & -x
    def update(index, d):
        while index <= q:
            fenwick[index] += d
            index += lowbit(index)
    def getsum(index):
        res = 0
        while index > 0:
            res += fenwick[index]
            index -= lowbit(index)
        return res

    size = 1
    tree = [[] for _ in range(q + 10)]
    node_create = [-1] * (q + 10)
    node_create[1] = 0
    tree_ops = [[] for _ in range(q + 10)]
    parents = [-1 for _ in range(q + 10)]
    for q_idx in range(1, q+1):
        query = inlt()
        if query[0] == 1:
            size += 1
            cur_node = query[1]
            node_create[size] = q_idx
            tree[cur_node].append(size)
            parents[size] = cur_node
        elif query[0] == 2:
            cur_node, val = query[1:]
            tree_ops[cur_node].append((val, q_idx))

    res = [0] * (size + 1)

    stack = []
    stack.append((1, 0))
    while stack:
        root, state = stack.pop()
        if state == 0:
            for val, q_idx in tree_ops[root]:
                update(q_idx, val)
            res[root] = getsum(q) - getsum(node_create[root])
            stack.append((root, 1))
            for nxt_node in tree[root]:
                stack.append((nxt_node, 0))
        if state == 1:
            for val, q_idx in tree_ops[root]:
                update(q_idx, -val)

    print(*res[1:])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()

