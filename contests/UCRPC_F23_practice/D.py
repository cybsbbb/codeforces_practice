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
    l, n, k = inlt()
    state = [0] * (l+5)
    ends = [[] for _ in range(l+5)]
    for _ in range(n):
        a, b, c, d = inlt()
        state[a] += 1
        ends[a].append(c + 1)
        state[c + 1] -= 1
    cur_end = []
    cur_val = 0
    res = 0

    for i in range(1, l+1):
        cur_val += state[i]
        for end in ends[i]:
            heapq.heappush(cur_end, -end)
        if cur_val > k:
            for _ in range(cur_val - k):
                res += 1
                cur_val -= 1
                max_end = heapq.heappop(cur_end)
                state[-max_end] += 1

    print(res)
    return


if __name__ == '__main__':
    # t = inp()
    for i in range(1):
        solution()
