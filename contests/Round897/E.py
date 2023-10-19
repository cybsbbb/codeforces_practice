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
    n, k = inlt()
    res = 0
    start = 1
    while n - start + 1 >= 2 * k:
        print(f"? {start}", flush=True)
        res ^= int(input())
        start += k
    if n - start + 1 == k:
        print(f"? {start}", flush=True)
        res ^= int(input())
    else:
        mid = (n - k + 1 - start) // 2
        print(f"? {start}", flush=True)
        res ^= int(input())
        print(f"? {start + mid}", flush=True)
        res ^= int(input())
        print(f"? {start + mid + mid}", flush=True)
        res ^= int(input())
    print("!", res, flush=True)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
