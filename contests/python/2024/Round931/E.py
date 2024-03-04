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
    n = inp()
    n_bin = bin(n)[2:][::-1]

    if n_bin.count('1') % 2 == 1:
        print(f"second", flush=True)
    else:
        print(f"first", flush=True)

        n_ones = []
        for i in range(len(n_bin)):
            if n_bin[i] == '1':
                n_ones.append(i)
        a = n_ones[-1]
        print(1 << a, n ^ (1 << a), flush=True)

    while True:
        p1, p2 = inlt()
        if p1 == 0 and p2 == 0:
            return
        p1_bin = bin(p1)[2:][::-1]
        p2_bin = bin(p2)[2:][::-1]
        if p1_bin.count('1') % 2 == 1:
            p1_bin, p2_bin = p2_bin, p1_bin
            p1, p2 = p2, p1

        p1_ones = []
        for i in range(len(p1_bin)):
            if p1_bin[i] == '1':
                p1_ones.append(i)
        a = p1_ones[-1]
        print(1 << a, p1 ^ (1 << a), flush=True)

    return





if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
