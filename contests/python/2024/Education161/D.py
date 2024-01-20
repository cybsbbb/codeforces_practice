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
    d = inlt()
    left = [-1] + list(range(n-1))
    right = list(range(1, n)) + [-1]
    res = [0] * n
    cur_candidate = set(range(n))
    for turn in range(n):
        if len(cur_candidate) == 0:
            break
        nxt_candidate = set()
        cur_remove = []
        for i in list(cur_candidate):
            left_i = left[i]
            right_i = right[i]
            attack = 0
            if left_i >= 0:
                attack += a[left_i]
            if right_i >= 0:
                attack += a[right_i]
            if attack > d[i]:
                cur_remove.append(i)
                if left_i >= 0:
                    nxt_candidate.add(left_i)
                if right_i >= 0:
                    nxt_candidate.add(right_i)

        res[turn] = len(cur_remove)

        for i in cur_remove:
            if i in nxt_candidate:
                nxt_candidate.remove(i)
            if left[i] >= 0:
                right[left[i]] = right[i]
            if right[i] >= 0:
                left[right[i]] = left[i]

        cur_candidate = nxt_candidate

    print(*res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
