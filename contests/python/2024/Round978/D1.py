import collections
import sys
import heapq
import math

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
    found = False
    fp1, fp2 = -1, -1
    for i in range(n // 2):
        p1, p2 = i * 2 + 1, i * 2 + 2
        print(f'? {p1} {p2}', flush=True)
        ans1 = inp()
        print(f'? {p2} {p1}', flush=True)
        ans2 = inp()
        if ans1 != ans2:
            found = True
            fp1, fp2 = p1, p2
            break
    if not found:
        print(f'! {n}', flush=True)
        return
    third_p = -1
    for i in range(1, n + 1):
        if i != fp1 and i != fp2:
            third_p = i
            break

    print(f'? {fp1} {third_p}', flush=True)
    ans1 = inp()
    print(f'? {third_p} {fp1}', flush=True)
    ans2 = inp()
    if ans1 != ans2:
        print(f'! {fp1}', flush=True)
        return

    print(f'? {fp2} {third_p}', flush=True)
    ans1 = inp()
    print(f'? {third_p} {fp2}', flush=True)
    ans2 = inp()
    if ans1 != ans2:
        print(f'! {fp2}', flush=True)
        return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
