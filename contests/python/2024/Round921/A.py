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
    n, k = inlt()
    ans = [chr(i + ord('a')) for i in range(k)]
    ans = ans * n
    print(''.join(ans))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
