import collections
import sys
import heapq
import bisect

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
    n, m, k = inlt()
    a = inlt()
    d = inlt()
    d.sort()
    f = inlt()
    f.sort()
    heap = []
    for i in range(n - 1):
        heapq.heappush(heap, (-(a[i + 1] - a[i]), i))
    max_idx = heap[0][1]
    left = a[max_idx]
    right = a[max_idx + 1]
    mid = left + (right - left + 1) // 2
    new_max = right - left
    for di in d:
        target = mid - di
        f_idx = bisect.bisect_left(f, target)
        if f_idx < k and left < di + f[f_idx] < right:
            new_max = min(new_max, max(right - (di + f[f_idx]), (di + f[f_idx]) - left))
        if f_idx - 1 >= 0 and left < di + f[f_idx - 1] < right:
            new_max = min(new_max, max(right - (di + f[f_idx - 1]), (di + f[f_idx - 1]) - left))

    heapq.heappop(heap)
    heapq.heappush(heap, (-new_max, n))
    print(-heap[0][0])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
