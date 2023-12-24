import collections
import heapq
import sys
input = sys.stdin.readline


def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


if __name__ == '__main__':
    n = inp()
    heap = []
    for i in range(n):
        candy = inp()
        heapq.heappush(heap, candy)

    res = 0
    while len(heap) > 1:
        candy1 = heapq.heappop(heap)
        candy2 = heapq.heappop(heap)
        res += (candy1 + candy2) * 2
        heapq.heappush(heap, (candy1 + candy2))
    print(res)
