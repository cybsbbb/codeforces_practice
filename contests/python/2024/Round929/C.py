
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
    a, b, l = inlt()
    ans = set()
    def find_b(val):
        ans.add(val)
        while val % b == 0:
            val //= b
            ans.add(val)
        return

    find_b(l)
    while l % a == 0:
        l //= a
        find_b(l)

    print(len(ans))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
