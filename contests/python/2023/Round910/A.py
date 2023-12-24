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
    n, k = inlt()
    s = input()[:-1]
    B_cnt = s.count('B')
    ans = 0
    if B_cnt == k:
        print(0)
        return
    elif B_cnt < k:
        ans_c = 'B'
        target_num = k - B_cnt
    else:
        ans_c = 'A'
        target_num = B_cnt - k
    print(1)
    cnt = 0
    for i in range(n):
        if s[i] != ans_c:
            cnt += 1
        if cnt == target_num:
            print(i + 1, ans_c)
            return
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
