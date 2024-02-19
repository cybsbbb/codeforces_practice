import sys

input = sys.stdin.buffer.readline


def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))
def insr():
    s = input()
    return (list(s[:len(s) - 1]))
def invr():
    return (map(int, input().split()))

MOD = 998244353


def comb(n, k):
    res = 1
    for i in range(k):
        res *= (n - i)
        res %= MOD
    for i in range(1, k + 1):
        res *= pow(i, -1, MOD)
        res %= MOD
    return res


for i in range(inp()):
    n, C = inlt()
    tree = [None for _ in range(n + 1)]
    for i in range(1, n + 1):
        tree[i] = inlt()

    queue = [1]
    st = [1]
    visited = [False] * (n + 1)
    while st:
        top = st[-1]
        if top == -1:
            st.pop()
            continue
        if not visited[top]:
            visited[top] = True
            st.append(tree[top][0])
        else:
            queue.append(tree[top][-1])
            st.pop()
            st.append(tree[top][1])
    queue.append(C)

    ans = 1
    i = 0
    while i < len(queue):
        j = i + 1
        while j < len(queue) and queue[j] == -1:
            j += 1
        if j == len(queue):
            break
        else:
            num_unknown = j - i - 1
            ans *= comb(queue[j] - queue[i] + num_unknown, num_unknown)
            ans %= MOD
            i = j
    print(ans)
