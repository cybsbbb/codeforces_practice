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
    s = insr()
    val = 0
    for i in range(n):
        cur_val = 1 if s[i] == '+' else -1
        val += cur_val

    print(abs(val))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
