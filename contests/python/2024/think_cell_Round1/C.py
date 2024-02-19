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


def solution():
    n = inp()
    a = inlt()
    intervals = []
    for i in range(n):
        intervals.append((a[i] + 1, a[i] + i + 1))
    intervals.sort(key=lambda X: (X[1], X[0]), reverse=True)
    # print(intervals)
    res = []
    left_heap = []
    pre = 10 ** 18
    for start, end in intervals:
        if pre - 1 >= end:
            res.append(end)
            heapq.heappush(left_heap, -start)
            pre = end
        elif pre - 1 >= start:
            heapq.heappush(left_heap, -start)
            res.append(pre - 1)
            pre = pre - 1
        else:
            while -left_heap[0] > pre - 1:
                heapq.heappop(left_heap)
            if left_heap:
                res.append(pre - 1)
                pre = pre - 1

    print(*res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
