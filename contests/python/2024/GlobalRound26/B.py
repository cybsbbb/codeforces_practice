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
    x = input()[:-1]
    n = len(x)
    if x[0] != '1' or x[-1] == '9':
        print("NO")
        return
    for i in range(1, n - 1):
        if x[i] == '0':
            print('NO')
            return
    print('YES')
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
