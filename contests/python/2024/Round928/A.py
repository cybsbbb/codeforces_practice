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
    s = insr()
    a_cnt = 0
    b_cnt = 0
    for i in range(5):
        if s[i] == 'A':
            a_cnt += 1
        else:
            b_cnt += 1
    if a_cnt > b_cnt:
        print("A")
    else:
        print("B")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
