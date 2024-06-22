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
    a = list(input()[:-1])
    b = list(input()[:-1])
    q = inp()
    a_final = a[:]
    b_final = b[:]
    for i in range(1, n - 1):
        if a_final[i - 1] == '0' and a_final[i + 1] == '0':
            b_final[i] = '1'
    for i in range(1, n - 1):
        if b_final[i - 1] == '1' and b_final[i + 1] == '1':
            a_final[i] = '1'
    prefix = [0]
    cur_cnt = 0
    for i in range(n):
        if a_final[i] == '1':
            cur_cnt += 1
        prefix.append(cur_cnt)

    for _ in range(q):
        l, r = inlt()
        if r - l + 1 < 5:
            a_tmp = a[l-1:r]
            b_tmp = b[l-1:r]
            for i in range(1, r - l):
                if a_tmp[i - 1] == '0' and a_tmp[i + 1] == '0':
                    b_tmp[i] = '1'
            for i in range(1, r - l):
                if b_tmp[i - 1] == '1' and b_tmp[i + 1] == '1':
                    a_tmp[i] = '1'
            ans = 0
            for i in range(r - l + 1):
                if a_tmp[i] == '1':
                    ans += 1
        else:
            ans = prefix[r - 2] - prefix[l + 1]
            # left
            a_tmp = a[l-1: l+4]
            b_tmp = b[l-1: l+4]
            for i in range(1, 4):
                if a_tmp[i - 1] == '0' and a_tmp[i + 1] == '0':
                    b_tmp[i] = '1'
            for i in range(1, 4):
                if b_tmp[i - 1] == '1' and b_tmp[i + 1] == '1':
                    a_tmp[i] = '1'
            for i in range(0, 2):
                if a_tmp[i] == '1':
                    ans += 1
            # right
            a_tmp = a[r - 5: r]
            b_tmp = b[r - 5: r]
            for i in range(1, 4):
                if a_tmp[i - 1] == '0' and a_tmp[i + 1] == '0':
                    b_tmp[i] = '1'
            for i in range(1, 4):
                if b_tmp[i - 1] == '1' and b_tmp[i + 1] == '1':
                    a_tmp[i] = '1'
            for i in range(3, 5):
                if a_tmp[i] == '1':
                    ans += 1
        print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





