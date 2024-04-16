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
    ans = 0
    for i in range(1, n + 1):
        ans += i * (2 * i - 1)
    permutations = []
    for i in range(1, n+1)[::-1]:
        permutations.append([1] + [i] + list(range(1, n + 1)))
        permutations.append([2] + [i] + list(range(1, n + 1)))
    print(ans, 2 * n)
    for j in range(2 * n):
        print(*permutations[j])

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
