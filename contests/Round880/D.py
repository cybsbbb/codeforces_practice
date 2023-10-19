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
    k = inp()
    galaxies = inlt()
    traits = {0: (-1, -1)}
    xor = 0
    res = [-1, -1, -1, -1]
    for i in range(2 * k + 1):
        xor ^= galaxies[i]
        if xor in traits:
            start, end = traits[xor]
            if res[0] == -1 or end - start + 1 + i - res[1] < res[3] - res[0] + 1 + res[2] - res[1]:
                res = [start + 1, end + 1, i + 1, i + 1]
        else:
            traits[xor] = (i, i)
    if res[0] != -1:
        print(*res)
    else:
        print(-1)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
