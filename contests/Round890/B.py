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
    if n == 1:
        print("NO")
        return 0

    cnt1 = 0
    extra = 0
    for num in a:
        if num == 1:
            cnt1 += 1
        else:
            extra += num - 1

    if cnt1 > extra:
        print("NO")
    else:
        print("YES")
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
