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
    p1, p2, p3, p4 = inlt()
    ans = 0
    ans += p1 // 2
    ans += p2 // 2
    ans += p3 // 2
    ans += p4 // 2
    if p1 % 2 == 1 and p2 % 2 == 1 and p3 % 2 == 1:
        ans += 1
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
