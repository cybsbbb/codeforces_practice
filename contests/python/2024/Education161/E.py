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
    X = inp()
    X_bin = bin(X)[2:][::-1]
    res = []
    for i in range(len(X_bin) - 1):
        res.append(2 * i + 1)
    for i in range(len(X_bin) - 1)[::-1]:
        if X_bin[i] == '1':
            res.append(2 * i)
    print(len(res))
    print(*res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
