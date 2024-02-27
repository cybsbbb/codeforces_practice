import bisect
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
    n, m, q = inlt()
    maps = ["0011110000111100",
            "1100001111000011",
            "0110100101101001",
            "1001011010010110",
            "1010101001010101",
            "1010010101011010",
            "0101010110101010",
            "0101101010100101",]
    stat = [True] * 8
    ans = 8
    print(ans)

    for _ in range(q):
        x, y, ind = input()[:-1].split()
        x = int(x) % 4
        y = int(y) % 4
        op = '0' if ind == 'circle' else '1'
        for i in range(8):
            if stat[i] is True:
                if maps[i][x * 4 + y] != op:
                    stat[i] = False
                    ans -= 1
        print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
