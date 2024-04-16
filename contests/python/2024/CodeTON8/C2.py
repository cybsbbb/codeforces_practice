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
    n, x, y = inlt()
    a = inlt()
    a.sort()
    ans = x - 2
    # intervals = []
    interval_odd = []
    interval_even = []
    for i in range(len(a) - 1):
        interval = a[i + 1] - a[i] - 1
        # intervals.append(interval)
        if interval > 0:
            if interval % 2 == 0:
                interval_even.append(interval)
            else:
                interval_odd.append(interval)

    interval = a[0] + n - a[-1] - 1
    # intervals.append(interval)
    if interval > 0:
        if interval % 2 == 0:
            interval_even.append(interval)
        else:
            interval_odd.append(interval)

    interval_odd.sort()
    for interval in interval_odd:
        require = interval // 2
        if require <= y:
            ans += interval
            y -= require
        else:
            ans += y * 2
            y -= y

    interval_even.sort()
    for interval in interval_even:
        require = interval // 2
        if require <= y:
            ans += interval
            y -= require
        else:
            ans += y * 2
            y -= y

    # intervals.sort()
    # for interval in intervals:
    #     require = interval // 2
    #     if require >= y:
    #         ans += interval
    #         y -= require
    #     else:
    #         ans += y
    #         y -= y

    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
