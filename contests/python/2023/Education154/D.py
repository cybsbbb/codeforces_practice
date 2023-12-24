
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
    dp_positive = [0] * n
    for i in range(1, n):
        if a[i] > a[i-1]:
            dp_positive[i] = dp_positive[i - 1]
        else:
            dp_positive[i] = dp_positive[i - 1] + 1
    positive_tot = dp_positive[-1]

    dp_negative = [0] * n
    dp_negative[0] = 1
    for i in range(1, n):
        if a[i] < a[i-1]:
            dp_negative[i] = dp_negative[i - 1]
        else:
            dp_negative[i] = dp_negative[i - 1] + 1
    negative_tot = dp_negative[-1]

    res = min(positive_tot, negative_tot)
    for i in range(n-1):
        res = min(res, dp_negative[i] + (positive_tot - dp_positive[i+1]))

    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
