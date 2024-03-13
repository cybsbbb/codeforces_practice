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
    n, m, k = inlt()
    b = inlt()
    c = inlt()
    b_cnt = collections.Counter(b)
    c_cnt = collections.Counter(c)
    res = 0
    for key_b in sorted(b_cnt.keys()):
        for key_c in sorted(c_cnt.keys()):
            if key_b + key_c <= k:
                res += b_cnt[key_b] * c_cnt[key_c]
            else:
                break
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
