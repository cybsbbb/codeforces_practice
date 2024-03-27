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
    a = inlt()
    cnt = collections.Counter(a)
    alice_num = 0
    one_found = False
    while cnt[alice_num] > 0:
        if cnt[alice_num] >= 2:
            alice_num += 1
        elif cnt[alice_num] == 1:
            if one_found is False:
                one_found = True
                alice_num += 1
            else:
                break
    print(alice_num)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
