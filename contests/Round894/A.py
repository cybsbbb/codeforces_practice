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
    carpet = []
    for _ in range(n):
        carpet.append(insr())
    cur_stage = 0
    targets = ['v', 'i', 'k', 'a']
    for i in range(m):
        if cur_stage == 4:
            break
        target_chr = targets[cur_stage]
        for j in range(n):
            if carpet[j][i] == target_chr:
                cur_stage += 1
                break
    if cur_stage == 4:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
