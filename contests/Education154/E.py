import math
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
    n, k = inlt()
    perm_num = math.factorial(k)
    rest_comb = pow(k, n - k - 1) * (k-1)
    print(perm_num * rest_comb * (n-k+1))


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
