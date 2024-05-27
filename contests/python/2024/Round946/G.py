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
    m, x = inlt()
    c = inlt()
    heap = []
    budget = 0
    for i in range(m):
        if budget >= c[i]:
            heapq.heappush(heap, -c[i])
            budget -= c[i]
        else:
            if heap and -heap[0] > c[i]:
                cur_max = heapq.heappop(heap)
                cur_max = -cur_max
                heapq.heappush(heap, -c[i])
                budget += cur_max - c[i]

        budget += x
    print(len(heap))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





