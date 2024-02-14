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
    graph = [[] for i in range(n)]
    ins = [0] * n
    for i in range(k):
        a = inlt()
        for j in range(2, n):
            graph[a[j - 1] - 1].append(a[j] - 1)
            ins[a[j] - 1] += 1

    q = collections.deque()
    for i in range(n):
        if ins[i] == 0:
            q.append(i)

    s = n
    while q:
        s -= 1
        u = q.popleft()
        for v in graph[u]:
            ins[v] -= 1
            if ins[v] == 0:
                q.append(v)

    if s == 0:
        print("YES")
    else:
        print("NO")

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
