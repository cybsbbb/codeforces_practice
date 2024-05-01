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


t = inp()
for _ in range(t):
    n, k = inlt()
    a = inlt()
    b = inlt()
    stat = sorted(zip(a, b), key=lambda x: (x[1], -x[0]), reverse=True)
    heap = []
    cost = 0
    for i in range(k):
        heapq.heappush(heap, -stat[i][0])
        cost += stat[i][0]
    profit = 0
    for i in range(k, n):
        profit += max(0, stat[i][1] - stat[i][0])

    ans = max(0, profit - cost)
    for i in range(k, n):
        if heap and -heap[0] > stat[i][0]:
            cost += heapq.heappop(heap)
            heapq.heappush(heap, -stat[i][0])
            cost += stat[i][0]
        profit -= max(0, stat[i][1] - stat[i][0])
        ans = max(ans, profit - cost)

    print(ans)

