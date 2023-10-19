import collections
import sys
import math
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def solution():
    s = insr()
    m = inp()
    l = insr()
    r = insr()
    n = len(s)

    num_set = set()
    cur_idx = 0

    for i in range(n):
        s_num = s[i]
        if l[cur_idx] <= s_num and s_num <= r[cur_idx]:
            num_set.add(s_num)
        if len(num_set) >= int(r[cur_idx]) - int(l[cur_idx]) + 1:
            cur_idx += 1
            num_set = set()
            if cur_idx >= m:
                break

    if cur_idx >= m:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
