import collections
import sys

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


for i in range(inp()):
    n = inp()
    a = inlt()
    cnt = collections.defaultdict(int)
    mask = (1 << 31) - 1

    for ai in a:
        if cnt[mask ^ ai]:
            cnt[mask ^ ai] -= 1
            n -= 1
        else:
            cnt[ai] += 1
    print(n)


