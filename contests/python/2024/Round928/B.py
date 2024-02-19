
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
    ones = []
    for i in range(n):
        ones.append(input()[:-1].count('1'))
    for i in range(1, n):
        if ones[i - 1] > 0 and ones[i - 1] == ones[i]:
            print("SQUARE")
            return
        if ones[i - 1] > 0 and ones[i] > 0 and ones[i - 1] != ones[i]:
            print("TRIANGLE")
            return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
