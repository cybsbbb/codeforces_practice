
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
    m, k, a1, ak = inlt()
    num_k_used = min(m // k, ak)
    m -= num_k_used * k
    if a1 >= m:
        print(0)
        return 0
    elif m < k:
        print(m-a1)
        return 0
    elif (m - a1) % k == 0:
        print((m - a1) // k)
        return 0
    else:
        num_k_fancy = (m - a1) // k
        res = num_k_fancy + (m - a1 - num_k_fancy * k)
        if m >= (num_k_fancy + 1) * k:
            res = min(res, num_k_fancy + 1)
        print(res)
        return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
