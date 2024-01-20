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
    forward = [0] * (n - 1)
    backward = [0] * (n - 1)
    forward[0] = a[1] - a[0] - 1
    backward[-1] = a[n-1] - a[n-2] - 1
    for i in range(1, n-1):
        if a[i + 1] - a[i] < a[i] - a[i - 1]:
            forward[i] = a[i + 1] - a[i] - 1
        else:
            backward[i-1] = a[i] - a[i - 1] - 1

    prefix_forward = [0]
    for v in forward:
        prefix_forward.append(prefix_forward[-1] + v)

    prefix_backward = [0]
    for v in backward:
        prefix_backward.append(prefix_backward[-1] + v)

    m = inp()
    for _ in range(m):
        xa, xb = inlt()
        xa -= 1
        xb -= 1
        if xa < xb:
            res = a[xb] - a[xa]
            res -= (prefix_forward[xb] - prefix_forward[xa])
            print(res)
        elif xa > xb:
            res = a[xa] - a[xb]
            res -= (prefix_backward[xa] - prefix_backward[xb])
            print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
