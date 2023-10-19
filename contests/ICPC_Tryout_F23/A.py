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
    h, w = inlt()
    map = []
    for i in range(h):
        map.append(insr())
    res = [0] * min(h, w)

    for i in range(h):
        for j in range(w):
            # if it is center
            if 0 < i < (h - 1) and 0 < j < (w - 1) and map[i][j] == '#':
                if map[i+1][j+1] == '#' and map[i+1][j-1] == '#' and map[i-1][j-1] == '#' and map[i-1][j+1] == '#':
                    n = 1
                    while 0 <= i + (n + 1) < h and 0 <= i - (n + 1) < h and 0 <= j + (n + 1) < w and 0 <= j - (n + 1) < w and \
                            map[i + (n + 1)][j + (n + 1)] == '#' and map[i + (n + 1)][j - (n + 1)] == '#' and \
                            map[i - (n + 1)][j - (n + 1)] == '#' and map[i - (n + 1)][j + (n + 1)] == '#':
                        n += 1
                    res[n - 1] += 1

    for n in res:
        print(n)
    # print(*res)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
