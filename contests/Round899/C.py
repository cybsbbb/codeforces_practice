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
    dp_odd = [-10**10] * n
    dp_even = [-10**10] * n
    dp_odd[0] = a[0]
    dp_even[0] = 0
    even = False
    for i in range(1, n):
        dp_odd[i] = dp_odd[i-1]
        dp_even[i] = dp_even[i-1]
        if (i + 1) % 2 == 1:
            dp_odd[i] = max(dp_odd[i], dp_even[i-1] + a[i])
            dp_even[i] = max(dp_even[i], dp_odd[i-1] + a[i], dp_odd[i-1])
            if dp_odd[i-1] + a[i] == dp_even[i]:
                even = True
        else:
            dp_odd[i] = max(dp_odd[i], dp_even[i-1])
            if even is True:
                dp_odd[i] = max(dp_odd[i], dp_even[i - 1] + a[i])
            dp_even[i] = max(dp_even[i], dp_odd[i-1] + a[i])
            if dp_odd[i-1] + a[i] == dp_even[i]:
                even = True

    res = max(max(dp_even), max(dp_odd))
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
