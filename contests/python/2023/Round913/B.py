
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
    s = insr()
    uppers = []
    lowers = []
    n = len(s)
    for i in range(n):
        cur = s[i]
        if cur.islower():
            if cur == 'b':
                if len(lowers):
                    lowers.pop()
            else:
                lowers.append((cur, i))
        else:
            if cur == 'B':
                if len(uppers):
                    uppers.pop()
            else:
                uppers.append((cur, i))
    ans = []
    lower_idx = 0
    upper_idx = 0
    while lower_idx < len(lowers) and upper_idx < len(uppers):
        if lowers[lower_idx][1] < uppers[upper_idx][1]:
            ans.append(lowers[lower_idx][0])
            lower_idx += 1
        else:
            ans.append(uppers[upper_idx][0])
            upper_idx += 1
    while lower_idx < len(lowers):
        ans.append(lowers[lower_idx][0])
        lower_idx += 1

    while upper_idx < len(uppers):
        ans.append(uppers[upper_idx][0])
        upper_idx += 1

    print(''.join(ans))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
