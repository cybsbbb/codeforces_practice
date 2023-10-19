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
    a, b, c = inlt()
    tot = a + b + c
    res = False
    for cut in range(4):
        final_cnt = 3 + cut
        if tot % final_cnt != 0:
            continue
        each_length = tot // final_cnt
        tot_cut = 0
        for cur in [a, b, c]:
            if cur % each_length != 0:
                tot_cut = 100
                break
            else:
                tot_cut += cur // each_length - 1
        if tot_cut <= cut:
            res = True

    if res == True:
        print("YES")
    else:
        print("NO")

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
