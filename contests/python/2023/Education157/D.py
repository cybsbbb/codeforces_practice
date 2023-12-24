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
    bits = [0] * 20
    prefix = [0]
    for ai in a:
        prefix.append(prefix[-1] ^ ai)
    for i in range(n):
        for bit in range(20):
            if (i >> bit) & 1:
                bits[bit] += 1
    b0 = 0
    for bit in range(20):
        cnt = 0
        for pre in prefix:
            if (pre >> bit) & 1:
                cnt += 1
        if cnt != bits[bit]:
            b0 += (1 << bit)

    res = [prefix[i] ^ b0 for i in range(n)]
    print(*res)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
