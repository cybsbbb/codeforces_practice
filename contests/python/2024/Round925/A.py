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
    n -= 3
    ans = []
    for i in range(3):
        if n >= 25:
            ans.append('z')
            n -= 25
        else:
            ans.append(chr(ord('a') + n))
            n -= n
    print(''.join(ans[::-1]))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
