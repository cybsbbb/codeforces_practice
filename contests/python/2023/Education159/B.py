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
    n, P, l, t = inlt()
    tot_task = (n + 6) // 7
    days_need = tot_task // 2
    if (l + 2 * t) * days_need >= P:
        print(n - (P - 1) // (l + 2 * t) - 1)
        return
    tot_task -= days_need * 2
    P -= (l + 2 * t) * days_need
    n -= days_need
    if tot_task == 1:
        if (l + t) >= P:
            print(n - 1)
            return
    P -= (l + t) * tot_task
    n -= tot_task
    print(n - (P - 1) // l - 1)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
