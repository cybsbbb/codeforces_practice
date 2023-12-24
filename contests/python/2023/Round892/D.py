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
    n = inp()
    intervals = []
    for i in range(n):
        li, ri, ai, bi = inlt()
        intervals.append((li, bi))
    intervals.sort()
    intervals_new = []
    cur_left, cur_right = intervals[0]
    idx = 1
    while idx < n:
        while idx < n and intervals[idx][0] <= cur_right:
            cur_right = max(cur_right, intervals[idx][1])
            idx += 1
        intervals_new.append((cur_left, cur_right))
        if idx < n:
            cur_left, cur_right = intervals[idx]
        else:
            cur_left, cur_right = -1, -1
    if cur_left > 0:
        intervals_new.append((cur_left, cur_right))
    intervals = intervals_new

    q = inp()
    x = inlt()
    q_heap = list(zip(x, range(q)))
    heapq.heapify(q_heap)
    res = [-1] * q

    for l, r in intervals:
        while q_heap and q_heap[0][0] < l:
            x, q_idx = heapq.heappop(q_heap)
            res[q_idx] = x

        while q_heap and q_heap[0][0] < r:
            x, q_idx = heapq.heappop(q_heap)
            heapq.heappush(q_heap, (r, q_idx))

        if len(q_heap) == 0:
            break

    while q_heap:
        x, q_idx = heapq.heappop(q_heap)
        res[q_idx] = x

    print(*res)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
