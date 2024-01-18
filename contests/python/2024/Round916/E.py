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
    n = inp()
    a = inlt()
    b = inlt()
    max_heap = []
    for i in range(n):
        heapq.heappush(max_heap, (-(a[i] + b[i]), i))

    ans = 0
    alice_turn = True
    while max_heap:
        if alice_turn:
            _, i = heapq.heappop(max_heap)
            ans += (a[i] - 1)
        else:
            _, i = heapq.heappop(max_heap)
            ans -= (b[i] - 1)
        alice_turn = not alice_turn
    print(ans)
    return ans


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
