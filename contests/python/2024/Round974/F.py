import collections
import sys
import heapq
import math

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
    n, c = inlt()
    a = inlt()
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = inlt()
        u -= 1
        v -= 1
        tree[u].append(v)
        tree[v].append(u)

    dp = [-10 ** 18] * (2 * n)
    queue = collections.deque()
    queue.append((0, -1, False))

    while queue:
        cur, par, flag = queue.pop()
        if flag is False:
            queue.append((cur, par, True))
            for nxt in tree[cur]:
                if nxt != par:
                    queue.append((nxt, cur, False))
        else:
            take = a[cur]
            no_take = 0
            for nxt in tree[cur]:
                if nxt != par:
                    take += max(dp[nxt] - 2 * c, dp[nxt + n])
                    no_take += max(dp[nxt], dp[nxt + n])
            dp[cur] = take
            dp[cur + n] = no_take

    ans = max(dp[0], dp[n])
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()

