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

def solve():
    n = inp()
    q = inlt()
    q.sort()
    cnt = collections.Counter(q)
    stat = [[key, val] for key, val in cnt.items()]
    stat.sort()

    heap = []
    budget = 0
    for key, val in cnt.items():
        if val <= budget:
            heapq.heappush(heap, -val)
            budget -= val
        else:
            budget += 1
            if heap and val < -heap[0]:
                old = heapq.heappop(heap)
                old = -old
                heapq.heappush(heap, -val)
                budget += old - val
    print(len(stat) - len(heap))
    return


t = inp()
for _ in range(t):
    solve()
