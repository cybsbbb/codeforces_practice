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
    n_bin = bin(n)[2:][::-1]
    m_bin = bin(m)[2:][::-1]
    if n_bin.count('1') == 1:
        print(-1)
        return
    n_ones = []
    for i in range(len(n_bin)):
        if n_bin[i] == '1':
            n_ones.append(i)
    m_ones = []
    for i in range(len(m_bin)):
        if m_bin[i] == '1':
            m_ones.append(i)

    a = n_ones[-1]
    b = n_ones[-2]
    c = m_ones[-1]

    if c < a and c > b:
        print(-1)
        return

    if c == a:
        print(1)
        print(n, m)
    else:
        if (1 << (b + 1)) - 1 == m:
            print(1)
            print(n, m)
        else:
            print(2)
            print(n, (1 << (b + 1)) - 1, m)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
