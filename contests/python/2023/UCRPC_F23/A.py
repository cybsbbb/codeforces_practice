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
    steps = []
    for _ in range(n):
        steps.append(inp())
    diffs = []
    for i in range(1, n):
        diffs.append(steps[i] - steps[i-1])
    diffs_cnt = collections.Counter(diffs)
    normal = max(zip(diffs_cnt.values(), diffs_cnt.keys()))[1]
    if diffs_cnt[normal] == n - 2:
        if steps[1] - steps[0] != normal:
            print(1)
            return
        if steps[-1] - steps[-2] != normal:
            print(n)
            return

    for i in range(1, n):
        if steps[i] - steps[i-1] != normal:
            print(i+1)
            return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
