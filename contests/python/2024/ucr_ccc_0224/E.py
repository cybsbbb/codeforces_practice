
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
    s = input()[:-1]
    res = []
    prefix = 0
    for i in range(n):
        prefix += ord(s[i]) - ord('0')
        res.append(prefix)
    res = res[::-1]
    while res[-1] == 0:
        res.pop()
    for i in range(len(res) - 1):
        res[i + 1] += res[i] // 10
        res[i] %= 10
    while res[-1] >= 10:
        res.append(res[-1] // 10)
        res[-2] %= 10

    print(''.join(map(str, res[::-1])))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
