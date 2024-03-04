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
    n, m = inlt()
    print(f"? 1 1", flush=True)
    dis11 = inp()
    if dis11 == 0:
        print(f"! 1 1", flush=True)
        return

    up_i, up_j = 1, 1 + dis11
    if up_j > m:
        up_i, up_j = 1 + (up_j - m), m

    down_i, down_j = 1 + dis11, 1
    if down_i > n:
        down_i, down_j = n, 1 + (down_i - n)

    # print(up_i, up_j)
    # print(down_i, down_j)

    print(f"? {up_i} {up_j}", flush=True)
    dis_up = inp()
    if dis_up == 0:
        print(f"! {up_i} {up_j}", flush=True)
        return

    print(f"? {down_i} {down_j}", flush=True)
    dis_down = inp()
    if dis_down == 0:
        print(f"! {down_i} {down_j}", flush=True)
        return

    candidate = []
    if dis_up % 2 == 0:
        can_i, can_j = up_i + dis_up // 2, up_j - dis_up // 2
        candidate.append((can_i, can_j))

    if dis_down % 2 == 0:
        can_i, can_j = down_i - dis_down // 2, down_j + dis_down // 2
        candidate.append((can_i, can_j))

    # print(candidate)

    print(f"? {candidate[0][0]} {candidate[0][1]}", flush=True)
    dis_cand1 = inp()
    if dis_cand1 == 0:
        print(f"! {candidate[0][0]} {candidate[0][1]}", flush=True)
        return
    else:
        print(f"! {candidate[1][0]} {candidate[1][1]}", flush=True)
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
