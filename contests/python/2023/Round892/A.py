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
    a = inlt()
    cnt = collections.Counter(a)
    if len(cnt) == 1:
        print(-1)
        return 0

    max_key = max(cnt.keys())
    c = [max_key] * cnt[max_key]
    b = []
    for key in cnt.keys():
        if key != max_key:
            for _ in range(cnt[key]):
                b.append(key)
    print(len(b), len(c))
    print(' '.join(map(str, b)))
    print(' '.join(map(str, c)))
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
