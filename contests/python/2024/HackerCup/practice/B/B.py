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


def solution(t):
    n, p = inlt()
    ans = pow(p / 100, (n - 1) / n) - p / 100
    print(f'Case #{t}: {ans * 100}')
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution(i + 1)
