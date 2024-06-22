import collections
import sys
import heapq
import math

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
    x, y, z, k = inlt()
    ans = [0]

    def helper(idx, cur_remain, cur_res):
        # print(idx, cur_remain, cur_res)
        if idx == 2:
            if cur_remain <= z:
                ans[0] = max(ans[0], cur_res * (z - cur_remain + 1))
            else:
                return
        else:
            cur_side = x if idx == 0 else y
            for val in range(1, cur_side + 1):
                if cur_remain % val == 0:
                    helper(idx + 1, cur_remain // val, cur_res * (cur_side - val + 1))

    helper(0, k, 1)
    print(ans[0])
    return




if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





