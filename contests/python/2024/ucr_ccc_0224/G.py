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


#   li + si * t == lj + sj * t (mod H)
#   (li - lj) == (sj - si) * t (mod H)


def solution():
    n, m, H = inlt()
    l = inlt()
    s = inlt()
    graph = collections.defaultdict(list)
    for _ in range(m):
        a, b = inlt()
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    dp = [float('inf')] * n
    dp[0] = 0
    queue = [(0, 0)]
    while queue:
        cur_time, cur_node = heapq.heappop(queue)
        if dp[cur_node] != cur_time:
            continue
        for nxt_node in graph[cur_node]:
            a = l[cur_node] - l[nxt_node]
            b = s[nxt_node] - s[cur_node]
            gcd = math.gcd(b, H)
            if a % gcd != 0:
                continue
            else:
                aa = a // gcd
                bb = b // gcd
                HH = H // gcd
                t = aa * pow(bb, -1, HH) % HH
                nxt_time = ((cur_time - t - 1) // HH + 1) * HH + t + 1
                if dp[nxt_node] > nxt_time:
                    dp[nxt_node] = nxt_time
                    heapq.heappush(queue, (nxt_time, nxt_node))

    if dp[-1] == float('inf'):
        print(-1)
    else:
        print(dp[-1])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
