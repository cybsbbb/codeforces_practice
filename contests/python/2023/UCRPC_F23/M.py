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
    eggs = []
    for _ in range(n):
        eggs.append(inlt())
    status = [False] * n
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            tmp_res = sum(eggs[i][f] < eggs[j][f] for f in range(k))
            if tmp_res >= k-1:
                status[j] = True
            if tmp_res == 1:
                status[i] = True

    print(sum(status))
    print(*[i+1 for i in range(n) if status[i] is True])
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
