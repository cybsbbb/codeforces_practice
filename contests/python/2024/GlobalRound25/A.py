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
    indexes = []
    for i in range(n):
        if s[i] == '1':
            indexes.append(i)

    if len(indexes) % 2 == 1:
        print("NO")
    elif len(indexes) == 2:
        if indexes[0] == indexes[1] - 1:
            print("NO")
        else:
            print("YES")
    else:
        print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
