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
    n, c = inlt()
    a = inlt()

    heap = [((i+1) * c - a[i], i) for i in range(1, n)]
    heapq.heapify(heap)

    cur_sum = a[0]
    while heap:
        diff, idx = heapq.heappop(heap)
        if diff - cur_sum > 0:
            print("No")
            return
        if idx == n-1:
            print("Yes")
            return
        cur_sum += a[idx]

    print("Yes")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
