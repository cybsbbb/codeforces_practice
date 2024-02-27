
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
    min_val = min(a)
    cnt = collections.Counter(a)
    if cnt[min_val] == 1:
        print("YES")
        return
    flag = False
    for val in cnt:
        if val == min_val:
            continue
        elif val % min_val != 0:
            flag = True
            break
    print("YES" if flag is True else "NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
