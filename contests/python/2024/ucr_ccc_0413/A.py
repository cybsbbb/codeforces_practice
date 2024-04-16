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
    ans = []
    for i in range(n):
        ans.append('1')
        ans.append('0')
    ans.append('1')
    print(''.join(ans))


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
