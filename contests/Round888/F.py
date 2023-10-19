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
    a = inlt()
    a_sorted = sorted(zip(a, range(1, n+1)))
    i = a_sorted[0][1]
    j = a_sorted[1][1]
    min_xor = a_sorted[1][0] ^ a_sorted[0][0]
    for idx in range(2, n):
        if a_sorted[idx][0] ^ a_sorted[idx-1][0] < min_xor:
            i = a_sorted[idx-1][1]
            j = a_sorted[idx][1]
            min_xor = a_sorted[idx][0] ^ a_sorted[idx-1][0]
    ai = a[i-1]

    x = ai ^ ((1 << k) - 1)
    print(i, j, x)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
