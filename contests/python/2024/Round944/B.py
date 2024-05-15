import collections
import sys
import heapq
import math

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
    if len(set(s)) == 1:
        print("NO")
        return
    print("YES")
    candidates1 = ''.join(sorted(list(s)))
    candidates2 = ''.join(sorted(list(s), reverse=True))
    if candidates1 != s:
        print(candidates1)
    else:
        print(candidates2)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





