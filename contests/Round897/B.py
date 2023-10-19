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
    s = insr()
    inPalindrome = 0
    res = [0] * (n+1)
    for i in range(n//2):
        if s[i] != s[-1-i]:
            inPalindrome += 1
    if n % 2 == 1:
        for i in range(inPalindrome, n + 1 - inPalindrome):
            res[i] = 1
    else:
        for i in range(inPalindrome, n + 1 - inPalindrome, 2):
            res[i] = 1

    print(''.join(map(str, res)))
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
