
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
    s = input()[:-1]
    n = len(s)
    if ')(' in s:
        print("YES")
        res = ['('] * n + [')'] * n
        print(''.join(res))
    else:
        if '()' in s and n == 2:
            print("NO")
        else:
            print("YES")
            res = ['()'] * n
            print(''.join(res))
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
