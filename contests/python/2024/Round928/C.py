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


N = 200000
ans = [0]
for i in range(1, N + 1):
    ans.append(ans[-1] + sum(map(int, str(i))))

for i in range(inp()):
    n = inp()
    print(ans[n])
