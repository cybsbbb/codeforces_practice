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

    a = 0
    max_b = a
    for b in range(n):
        print(f"? {a} {max_b} {a} {b}", flush=True)
        ind = input()[:-1]
        if ind == '<':
            max_b = b

    max_a = max_b
    candidates = [max_a]
    for a in range(n):
        print(f"? {max_a} {max_b} {a} {max_b}", flush=True)
        ind = input()[:-1]
        if ind == '<':
            max_a = a
            candidates = [max_a]
        elif ind == '=':
            candidates.append(a)

    min_max_a = candidates[0]
    for candidate in candidates[1:]:
        print(f"? {min_max_a} {min_max_a} {candidate} {candidate}", flush=True)
        ind = input()[:-1]
        if ind == '>':
            min_max_a = candidate

    print(f"! {max_b} {min_max_a}", flush=True)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
