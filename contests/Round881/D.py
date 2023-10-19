import sys
sys.setrecursionlimit(200000)

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
    n = inp()
    tree = [[] for _ in range(n+1)]
    for i in range(n-1):
        a, b = inlt()
        tree[a].append(b)
        tree[b].append(a)
    q = inp()
    queries = []
    for i in range(q):
        queries.append(inlt())

    leaves = [0] * (n + 1)

    stack = []
    for node in tree[1]:
        stack.append((node, 1))
    seen = set()
    seen.add(1)

    while len(stack) > 0:
        top_node, pre = stack[-1]
        if len(tree[top_node]) == 1:
            leaves[top_node] += 1
            leaves[pre] += leaves[top_node]
            stack.pop()
        elif top_node not in seen:
            seen.add(top_node)
            for node in tree[top_node]:
                if node not in seen:
                    stack.append((node, top_node))
        elif top_node in seen:
            leaves[pre] += leaves[top_node]
            stack.pop()

    for x, y in queries:
        print(leaves[x] * leaves[y])


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
