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
    ans = 0
    cnt_a = collections.Counter(a)
    for v in cnt_a.values():
        ans += v // 3
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
