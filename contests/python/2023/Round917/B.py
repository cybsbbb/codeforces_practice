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
    s = insr()
    ans = 0
    pre_c = set()
    pre_c.add(s[0])
    for i in range(1, n):
        ans += (len(pre_c))
        pre_c.add(s[i])
    ans += (len(pre_c))
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
