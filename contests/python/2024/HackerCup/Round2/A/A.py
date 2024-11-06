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

peaks = []
for l in range(1, 18, 2):
    for st in range(1, 10 - l // 2):
        tmp = list(map(str, range(st, st + (l + 1) // 2))) + list(map(str, range(st, st + l // 2)[::-1]))
        peaks.append(int(''.join(tmp)))

def solution(ttt):
    A, B, M = inlt()
    ans = 0
    for peak in peaks:
        if A <= peak <= B and peak % M == 0:
            ans += 1
    print(f"Case #{ttt}: {ans}")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution(i + 1)
