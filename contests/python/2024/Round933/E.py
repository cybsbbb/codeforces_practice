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
    n, m, k, d = inlt()
    river = []
    for i in range(n):
        river.append(inlt())

    def helper(line):
        heap = [(1, 0)]
        for i in range(1, m):
            while i - heap[0][1] - 1 > d:
                heapq.heappop(heap)
            cur_res = line[i] + 1 + heap[0][0]
            heapq.heappush(heap, (cur_res, i))
            if i == m - 1:
                return cur_res

    costs = [helper(river[i]) for i in range(n)]
    tmp = sum(costs[:k])
    res = tmp
    for i in range(n - k):
        tmp -= costs[i]
        tmp += costs[i + k]
        res = min(res, tmp)
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
