import collections
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


for i in range(inp()):
    n = inp()
    a = inlt()
    s = input()[:-1]
    tree = collections.defaultdict(list)
    for i in range(n - 1):
        tree[i + 1].append(a[i] - 1)
        tree[a[i] - 1].append(i + 1)

    dp = [[float('inf')] * 3 for i in range(n)]

    st = [(0, -1, False)]
    while st:
        cur_node, cur_par, cur_flag = st.pop()
        if cur_flag is False:
            st.append((cur_node, cur_par, True))
            for nxt_node in tree[cur_node]:
                if nxt_node != cur_par:
                    st.append((nxt_node, cur_node, False))
        else:
            if s[cur_node] == 'P':
                dp[cur_node][0] = 0
                for nxt_node in tree[cur_node]:
                    if nxt_node != cur_par:
                        dp[cur_node][0] += min(dp[nxt_node][0], dp[nxt_node][1] + 1, dp[nxt_node][2])
            elif s[cur_node] == 'S':
                dp[cur_node][1] = 0
                for nxt_node in tree[cur_node]:
                    if nxt_node != cur_par:
                        dp[cur_node][1] += min(dp[nxt_node][0] + 1, dp[nxt_node][1], dp[nxt_node][2])
            elif s[cur_node] == 'C':
                dp[cur_node][0] = 0
                dp[cur_node][1] = 0
                dp[cur_node][2] = 0
                for nxt_node in tree[cur_node]:
                    if nxt_node != cur_par:
                        dp[cur_node][0] += min(dp[nxt_node][0], dp[nxt_node][1] + 1, dp[nxt_node][2])
                        dp[cur_node][1] += min(dp[nxt_node][0] + 1, dp[nxt_node][1], dp[nxt_node][2])
                        dp[cur_node][2] += min(dp[nxt_node][0] + 1, dp[nxt_node][1] + 1, dp[nxt_node][2])

    ans = min(dp[0])
    print(ans)
