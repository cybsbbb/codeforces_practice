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
    n, k = inlt()
    s = insr()
    if k % 2 == 0:
        print(''.join(sorted(s)))
        return
    else:
        even = sorted([s[i] for i in range(0, n, 2)])
        odd = sorted([s[i] for i in range(1, n, 2)])
        res = [0] * n
        for i in range(len(even)):
            res[2*i] = even[i]
        for i in range(len(odd)):
            res[2*i + 1] = odd[i]
        print(''.join(res))
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
