import collections
import sys
import math
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def solution():
    n, k = inlt()
    left = 1
    right = n
    res = 0
    while left < right:
        res += 2
        left += k
        right -= k

    if right - left + 2 * k - 1 >= k:
        res += 1

    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
