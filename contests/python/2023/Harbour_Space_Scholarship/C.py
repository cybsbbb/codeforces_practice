import collections
import math
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
    x = inp()
    ans = []
    ans.append(1)
    while ans[-1] * 2 <= x:
        ans.append(ans[-1] * 2)
    if ans[-1] == x:
        print(len(ans))
        print(*ans[::-1])
        return
    tmp = ans[-1] // 2
    while tmp >= 1:
        if ans[-1] + tmp <= x:
            ans.append(ans[-1] + tmp)
        tmp = tmp // 2
        if ans[-1] == x:
            break
    print(len(ans))
    print(*ans[::-1])
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
