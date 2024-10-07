import collections
import sys
import heapq
import math
import random

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


hash_val = [random.randint(0, 1 << 63) for x in range(10**6+1)]

def solution():
    n, q = inlt()
    a = inlt()
    stats = [0]
    for i in range(n):
        stats.append(stats[-1] ^ hash_val[a[i]])
    for _ in range(q):
        l, r = inlt()
        if stats[r] == stats[l - 1]:
            print("YES")
        else:
            print("NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()

