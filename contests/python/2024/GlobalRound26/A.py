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
    if a[0] == a[-1]:
        print("NO")
        return
    elif a[1] != a[-1]:
        ans = ['R'] + ['B'] * (n - 1)
        print('YES')
        print(''.join(ans))
        return
    else:
        ans = ['B'] * (n - 1) + ['R']
        print('YES')
        print(''.join(ans))
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
