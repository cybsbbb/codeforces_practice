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
    cur_val = a[-1]
    for ai in a[::-1]:
        if ai <= cur_val:
            cur_val = ai
        else:
            if ai < 10:
                print("NO")
                return
            else:
                first, second = ai // 10, ai % 10
                if first > second or second > cur_val:
                    print("NO")
                    return
                else:
                    cur_val = first
    print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
