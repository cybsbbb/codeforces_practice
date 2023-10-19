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
    p = [-1] + inlt()
    graph = collections.defaultdict(list)
    for i in range(1, n):
        graph[p[i]].append(i+1)

    res = [0]
    def dfs(root):
        pass



if __name__ == '__main__':
    # t = inp()
    for i in range(1):
        solution()
