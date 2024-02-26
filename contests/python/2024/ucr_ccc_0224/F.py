
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
    n, m = inlt()
    cats = []
    for i in range(m):
        cats.append(inlt())
    cats.sort()
    dp = [0] * (n + 1)
    cat_idx = 0
    heap_interval = []
    heap_end = []
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        while heap_interval and heap_interval[0][1] < i:
            heapq.heappop(heap_interval)
        while heap_end and heap_end[0] < i:
            heapq.heappop(heap_end)
        while cat_idx < m and cats[cat_idx][0] == i:
            heapq.heappush(heap_interval, cats[cat_idx])
            heapq.heappush(heap_end, cats[cat_idx][1])
            cat_idx += 1
        if heap_interval:
            dp[i] = max(dp[i], dp[heap_interval[0][0] - 1] + len(heap_end))

    print(dp[-1])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
