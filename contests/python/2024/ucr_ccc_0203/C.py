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

# 1 2 2 3 4 4


def solution():
    n, k = inlt()
    a = inlt()
    a_set = set(a)
    socks = []
    for i in range(1, n + 1):
        socks.append(i)
        if i not in a_set:
            socks.append(i)
    m = len(socks)
    if m == 1:
        print(0)
        return

    if m % 2 == 0:
        ans = 0
        for i in range(m // 2):
            ans += socks[2 * i + 1] - socks[2 * i]

    elif m % 2 == 1:
        front = [0]
        end = [0]
        for i in range(m // 2):
            front.append(front[-1] + socks[2 * i + 1] - socks[2 * i])
        for i in range(m // 2)[::-1]:
            end.append(end[-1] + socks[2 * i + 2] - socks[2 * i + 1])
        front = front[1:]
        end = end[1:][::-1]

        ans = min(front[-1], end[0])
        for i in range(m // 2 - 1):
            ans = min(ans, front[i] + end[i + 1])

    print(ans)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
