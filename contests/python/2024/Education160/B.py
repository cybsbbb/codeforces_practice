
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
    cnt = collections.Counter(s)
    for i in range(n):
        if s[i] == '0' and cnt['1'] > 0:
            cnt['1'] -= 1
        elif s[i] == '1' and cnt['0'] > 0:
            cnt['0'] -= 1
        else:
            print(n - i)
            return
    print(0)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
