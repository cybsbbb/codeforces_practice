import sys
import heapq
import itertools

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


n, m = inlt()
dist = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
edges = []
for i in range(m):
    ui, vi, ti = inlt()
    ui -= 1
    vi -= 1
    edges.append((ui, vi, ti))
    dist[ui][vi] = min(dist[ui][vi], ti)
    dist[vi][ui] = min(dist[vi][ui], ti)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

q = inp()
ans = []
for _ in range(q):
    k = inp()
    b = inlt()
    ans_sub = float('inf')
    for perm in itertools.permutations(range(k)):
        left_pre, right_pre = 0, 0
        left_pre_cost, right_pre_cost = 0, 0
        for i in range(k):
            ui, vi, ti = edges[b[perm[i]] - 1]
            left_nxt_cost = min(left_pre_cost + dist[left_pre][vi] + ti, right_pre_cost + dist[right_pre][vi] + ti)
            right_nxt_cost = min(left_pre_cost + dist[left_pre][ui] + ti, right_pre_cost + dist[right_pre][ui] + ti)
            left_pre_cost, right_pre_cost = left_nxt_cost, right_nxt_cost
            left_pre, right_pre = ui, vi
        ans_sub = min(ans_sub, left_pre_cost + dist[left_pre][n - 1], right_pre_cost + dist[right_pre][n - 1])
    print(ans_sub)




