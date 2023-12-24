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
    a_counter = collections.Counter(a)
    cur_key = 0
    pre_num = float('inf')
    for key in sorted(a_counter.keys()):
        if key != cur_key:
            print("NO")
            return
        if a_counter[key] > pre_num:
            print("NO")
            return
        pre_num = a_counter[key]
        cur_key = key + 1

    print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
