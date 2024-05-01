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


t = inp()
for i in range(t):
    n = inp()
    a = inlt()
    a = [0] + sorted(list(set(sorted(a))))

    cur_i = 1
    while cur_i < len(a) and a[cur_i] - a[cur_i - 1] == 1:
        cur_i += 1

    if cur_i == len(a):
        if len(a) % 2 == 0:
            print("Alice")
        else:
            print("Bob")
    else:
        if cur_i % 2 == 1:
            print("Alice")
        else:
            print("Bob")

    # if a[1] > 1:
    #     print("Alice")
    #     continue
    # ones = 0
    # more_ones = 0
    # for i in range(1, len(a)):
    #     val = a[i] - a[i - 1]
    #     if val == 1:
    #         ones += 1
    #     else:
    #         more_ones += 1
    # if ones % 2 == 1:
    #     if more_ones > 0:
    #         print("Bob")
    #     else:
    #         print("Alice")
    # else:
    #     if more_ones > 0:
    #         print("Alice")
    #     else:
    #         print("Bob")
