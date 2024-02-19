
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
    k, x, a = inlt()
    acc_loss = 0
    for i in range(x + 1):
        cur_bid = acc_loss // (k - 1) + 1
        acc_loss += cur_bid
    if acc_loss <= a:
        print("YES")
    else:
        print("NO")

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
