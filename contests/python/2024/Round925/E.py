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
    a = input().split()
    tot = 0
    ends = []
    for ai in a:
        tot += len(ai)
        end_zero = 0
        while ai[-1 - end_zero] == '0':
            end_zero += 1
        ends.append(end_zero)
    ends.sort(reverse=True)
    for i in range(0, n, 2):
        tot -= ends[i]

    if tot >= m + 1:
        print("Sasha")
    else:
        print("Anna")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
