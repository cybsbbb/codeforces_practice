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
    pos = insr()
    ans = []
    for first in 'abcdefgh':
        if first != pos[0]:
            ans.append(first + pos[1])
    for second in '12345678':
        if second != pos[1]:
            ans.append(pos[0] + second)

    for p in ans:
        print(p)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
