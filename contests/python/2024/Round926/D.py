
import collections
import sys
import heapq

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
    tree = [[] for i in range(n)]
    for i in range(n - 1):
        u, v = inlt()
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)

    MOD = 998244353

    dp = [1] * n
    st = [(0, -1, False)]
    while st:
        cur, par, flag = st.pop()
        if not flag:
            st.append((cur, par, True))
            for nxt in tree[cur]:
                if nxt != par:
                    st.append((nxt, cur, False))
        else:
            for nxt in tree[cur]:
                if nxt != par:
                    dp[cur] = dp[cur] * (1 + dp[nxt]) % MOD

    ans = 1
    for i in range(n):
        ans = (ans + dp[i]) % MOD

    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
