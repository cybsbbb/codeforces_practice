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
    a, b, c = inlt()
    ans = a
    ans += b // 3
    b = b % 3
    if b > 0:
        if b + c < 3:
            print(-1)
            return
        else:
            ans += 1
            c -= (3 - b)
    ans += (c + 2) // 3
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
