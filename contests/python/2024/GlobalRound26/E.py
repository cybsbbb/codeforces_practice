
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
    tree = [[] for i in range(n)]
    degree = [0] * n
    for _ in range(n - 1):
        u, v = inlt()
        u -= 1
        v -= 1
        tree[u].append(v)
        tree[v].append(u)
        degree[u] += 1
        degree[v] += 1

    leaves = collections.deque()
    for i in range(n):
        if degree[i] == 1:
            leaves.append(i)
    ans = len(leaves)








if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
