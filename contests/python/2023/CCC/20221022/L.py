import math
import sys

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


if __name__ == '__main__':
    n = inp()
    stats = [0] * (n + 1)

    for i in range(n):
        a, b = inlt()
        for j in range(a, b + 1):
            stats[j] += 1

    flag = False
    for j in range(n, -1, -1):
        if stats[j] == j:
            print(j)
            flag = True
            break
    if flag is False:
        print(-1)
