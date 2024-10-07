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
    n = inp()
    cur_ans = ""
    while len(cur_ans) < n:
        print(f"? {cur_ans + '1'}", flush=True)
        if inp() == 1:
            cur_ans += '1'
            continue
        print(f"? {cur_ans + '0'}", flush=True)
        if inp() == 1:
            cur_ans += '0'
            continue
        else:
            break
    while len(cur_ans) < n:
        print(f"? {'1' + cur_ans}", flush=True)
        if inp() == 1:
            cur_ans = '1' + cur_ans
        else:
            cur_ans = '0' + cur_ans

    print(f"! {cur_ans}", flush=True)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





