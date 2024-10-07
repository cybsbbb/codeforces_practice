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


n = inp()
a = inlt()
heap = []
for ai in a:
    heapq.heappush(heap, -ai)
ans = 0
while len(heap) > 1:
    ans += 1
    top1 = heapq.heappop(heap)
    top2 = heapq.heappop(heap)
    top1 += 1
    top2 += 1
    if top1 < 0:
        heapq.heappush(heap, top1)
    if top2 < 0:
        heapq.heappush(heap, top2)
print(ans)
