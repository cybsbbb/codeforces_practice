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
    n, l = inlt()
    messages = []
    for i in range(n):
        messages.append(inlt())
    messages.sort(key=lambda x: x[::-1])

    res = 0
    for start in range(n):
        remain_l = l
        remain_l -= messages[start][0]
        if remain_l < 0:
            continue
        cur_res = 1
        res = max(res, cur_res)
        a_heap = []
        a_sum = 0
        for i in range(start + 1, n):
            ai, bi = messages[i]
            remain_l -= (bi - messages[i - 1][1])
            heapq.heappush(a_heap, -ai)
            a_sum += ai
            while a_heap and a_sum > remain_l:
                a_sum -= (-heapq.heappop(a_heap))
            res = max(res, len(a_heap) + 1)

    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
