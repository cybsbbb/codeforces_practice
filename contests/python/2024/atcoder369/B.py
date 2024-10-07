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


n = inp()
left = []
right = []
for _ in range(n):
    ai, si = input()[:-1].split()
    if si == 'L':
        left.append(int(ai))
    else:
        right.append(int(ai))

ans = 0
for i in range(1, len(left)):
    ans += abs(left[i] - left[i - 1])
for i in range(1, len(right)):
    ans += abs(right[i] - right[i - 1])
print(ans)
