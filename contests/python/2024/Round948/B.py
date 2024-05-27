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
    x = inp()
    binary = bin(x)[2:][::-1]
    ans = []
    begin = -1
    cur_len = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            if cur_len == 0:
                begin = i
                cur_len = 1
            else:
                cur_len += 1
        elif binary[i] == '0':
            if cur_len == 0:
                ans.append(0)
            elif cur_len == 1:
                ans.append(1)
                ans.append(0)
                cur_len = 0
            else:
                ans.append(-1)
                for _ in range(cur_len - 1):
                    ans.append(0)
                    begin = i
                    cur_len = 1

    if cur_len == 1:
        ans.append(1)
    elif cur_len > 1:
        ans.append(-1)
        for _ in range(cur_len - 1):
            ans.append(0)
        ans.append(1)

    print(len(ans))
    print(*ans)
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





