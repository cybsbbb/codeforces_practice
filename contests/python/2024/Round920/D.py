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
    n, m = inlt()
    a = inlt()
    b = inlt()
    a.sort()
    b.sort()

    from_begin = [0]
    from_end = [0]
    for i in range(n):
        from_begin.append(from_begin[-1] + abs(a[i] - b[-1 - i]))
        from_end.append(from_end[-1] + abs(a[-1 - i] - b[i]))
    from_begin = from_begin[1:]
    from_end = from_end[1:][::-1]

    res = max(from_begin[-1], from_end[0])
    for i in range(n - 1):
        res = max(res, from_begin[i] + from_end[i+1])
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
