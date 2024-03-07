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
    n, m, l = inlt()
    a = inlt()
    a = sorted(zip(a, range(1, n + 1)), reverse=True)
    b = inlt()
    b = sorted(zip(b, range(1, m + 1)), reverse=True)

    no_offer = set()
    for i in range(l):
        ci, di = inlt()
        no_offer.add((ci, di))

    ans = 0
    for a_val, a_idx in a:
        for b_val, b_idx in b:
            if (a_idx, b_idx) in no_offer:
                continue
            else:
                ans = max(ans, a_val + b_val)
                break
    print(ans)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()