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
    b = inlt()
    product = 1
    for bi in b:
        product *= bi
    if 2023 % product != 0:
        print("No")
    else:
        print("Yes")
        ans = [2023 // product] + [1] * (k - 1)
        print(*ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
