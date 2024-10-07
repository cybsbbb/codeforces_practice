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


def solution():
    n = inp()
    s = input()[:-1]
    counter = collections.Counter(s)
    heap = []
    for cnt, c in list(zip(counter.values(), counter.keys())):
        heapq.heappush(heap, (-cnt, c))

    ans = []
    while len(heap) > 0:
        if len(heap) == 1:
            cnt, c = heapq.heappop(heap)
            cnt = -cnt
            ans += [c] * cnt
        else:
            cnt1, c1 = heapq.heappop(heap)
            cnt1 = -cnt1
            cnt2, c2 = heapq.heappop(heap)
            cnt2 = -cnt2
            ans.append(c1)
            cnt1 -= 1
            ans.append(c2)
            cnt2 -= 1
            if cnt1 > 0:
                heapq.heappush(heap, (-cnt1, c1))
            if cnt2 > 0:
                heapq.heappush(heap, (-cnt2, c2))

    print(''.join(ans))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





