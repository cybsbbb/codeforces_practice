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
    p = inlt()
    ans = sum(p[i] // 2 for i in range(4))
    if p[0] % 2 == 1 and p[1] % 2 == 1 and p[2] % 2 == 1:
        ans += 1
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
