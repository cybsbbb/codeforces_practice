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
    Sheldon = insr()
    Raj = insr()
    dp_cur = list(range(n+1))
    dp_nxt = [0] * (n + 1)

    for i in range(1, n+1):
        dp_nxt[0] = i
        for j in range(max(1, i - 100), min(n+1, i + 100)):
            dp_nxt[j] = min(dp_cur[j-1] + 1, dp_cur[j] + 1, dp_nxt[j-1] + 1)
            if Sheldon[i-1] == Raj[j-1]:
                dp_nxt[j] = min(dp_nxt[j], dp_cur[j-1])
        dp_cur, dp_nxt = dp_nxt, dp_cur

    print(dp_cur[-1])
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
