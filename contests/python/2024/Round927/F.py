import collections
import heapq
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
    n, m = inlt()
    intervals = []
    for i in range(m):
        intervals.append(inlt())

    intervals.sort()
    dp = [0] * (n + 1)
    heap = []
    heap_end = []
    cat_idx = 0
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        while heap_end and heap_end[0] < i:
            heapq.heappop(heap_end)
        while heap and heap[0][1] < i:
            heapq.heappop(heap)
        while cat_idx < m and intervals[cat_idx][0] <= i:
            heapq.heappush(heap, intervals[cat_idx])
            heapq.heappush(heap_end, intervals[cat_idx][1])
            cat_idx += 1
        if heap:
            dp[i] = max(dp[i], dp[heap[0][0] - 1] + len(heap_end))

    print(dp[n])
