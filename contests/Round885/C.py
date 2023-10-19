
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


def helper(a, b):
    if a == 0 and b == 0:
        return {0, 1, 2}
    cur = 0
    if a == 0:
        return {cur}
    if b == 0:
        return {(cur + 1) % 3}
    if a > b:
        a -= (a // (b * 2)) * (b * 2)
        if a == 0:
            return {cur}
    elif b > a:
        b -= (b // (a * 2)) * (a * 2)
        if b == 0:
            return {(cur + 1) % 3}
    while True:
        a, b = b, abs(a - b)
        cur = (cur + 1) % 3
        if a == 0:
            return {cur}
        if b == 0:
            return {(cur + 1) % 3}
        if a > b:
            a -= (a // (b * 2)) * (b * 2)
            if a == 0:
                return {cur}
        elif b > a:
            b -= (b // (a * 2)) * (a * 2)
            if b == 0:
                return {(cur + 1) % 3}


def solution():
    n = inp()
    a = inlt()
    b = inlt()
    zeros = {0, 1, 2}
    res = 'Yes'
    for i in range(n):
        zeros = zeros & helper(a[i], b[i])
        if len(zeros) == 0:
            res = 'No'
            break
    print(res)
    return 0




if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
