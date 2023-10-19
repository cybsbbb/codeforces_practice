import collections
import sys
import math
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def solution():
    k = inp()
    seeds = inlt()
    res = 1

    for cur_k in range(k-1, 0, -1):
        cur_bucket = 1 << (k - cur_k)
        cur_start = 1 << cur_k
        cur_end = 1 << (cur_k+1)
        teams = [2] * cur_start
        unset = 0
        for i in range(cur_start, cur_end):
            if seeds[i] != -1:
                teams[i % cur_bucket] -= 1
                if teams[i % cur_bucket] == 0:
                    print(0)
                    return
            else:
                unset += 1
        for i in range(cur_start):
            if seeds[i] != -1:
                teams[i % cur_bucket] -= 1
                if teams[i % cur_bucket] < 0:
                    print(0)
                    return







if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
