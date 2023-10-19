import collections
import math
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
    if n == 1:
        print(2)
        return
    x = int(math.sqrt(2 * n))
    while (x * (x-1)) // 2 <= n:
        x += 1
    x -= 1
    res = x
    res += n - (x * (x-1) // 2)
    print(res)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
