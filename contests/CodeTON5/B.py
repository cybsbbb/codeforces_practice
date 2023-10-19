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


def num_set(num):
    res = set()
    for i in range(32):
        if (1 << i) & num != 0:
            res.add(i)
    return res


def solution():
    n, x = inlt()
    a = inlt()
    b = inlt()
    c = inlt()
    target = num_set(x)

    final = set()
    for num in a:
        tmp_set = num_set(num)
        if tmp_set <= target:
            final.update(tmp_set)
        else:
            break

    for num in b:
        tmp_set = num_set(num)
        if tmp_set <= target:
            final.update(tmp_set)
        else:
            break

    for num in c:
        tmp_set = num_set(num)
        if tmp_set <= target:
            final.update(tmp_set)
        else:
            break

    if final == target:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
