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


def solution():
    n, m = inlt()
    graph_back = collections.defaultdict(list)
    begins = collections.Counter()
    ins = collections.defaultdict(int)
    for _ in range(n):
        a = inlt()
        a_set = set(a[1:])
        flag = False
        first = -1
        second = -1
        for i in range(2 * 10 ** 5 + 5):
            if i not in a_set:
                if flag is False:
                    first = i
                    flag = True
                else:
                    second = i
                    break
        begins[first] += 1
        graph_back[second].append(first)
        ins[first] += 1
        ins[second] += 0

    dp = collections.defaultdict(int)
    queue = collections.deque()

    for key, value in ins.items():
        if value == 0:
            queue.append(key)

    while queue:
        cur = queue.popleft()
        for nxt in graph_back[cur]:
            dp[nxt] = max(dp[nxt], cur, dp[cur])
            ins[nxt] -= 1
            if ins[nxt] == 0:
                queue.append(nxt)

    max_reachable = max(begins.keys())
    for start, cnt in begins.items():
        if cnt > 1:
            max_reachable = max(max_reachable, dp[start])

    max_dp_val = max(dp.values())

    ans = 0
    for i in range(min(m, max_dp_val) + 1):
        ans += max(i, max_reachable, dp[i])
    if m > max_dp_val:
        ans += (max_dp_val + 1 + m) * (m - max_dp_val) // 2
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





