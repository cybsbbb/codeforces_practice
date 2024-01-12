
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
    m = inp()
    stat = [0 for i in range(50)]
    for i in range(m):
        ti, vi = inlt()
        # Add
        if ti == 1:
            stat[vi] += 1
            cur_idx = vi
            while stat[cur_idx] > 2:
                proceed_nxt = stat[cur_idx] // 2
                stat[cur_idx] -= proceed_nxt * 2
                stat[cur_idx + 1] += proceed_nxt
                cur_idx += 1
        # Query
        if ti == 2:
            binary_rep = list(map(int, bin(vi)[2:][::-1]))
            pre_v = 0
            flag = True
            for i in range(len(binary_rep)):
                cur_v = pre_v + stat[i]
                if cur_v < binary_rep[i]:
                    flag = False
                    break
                pre_v = (cur_v - binary_rep[i]) // 2
            print("YES" if flag else "NO")

    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
