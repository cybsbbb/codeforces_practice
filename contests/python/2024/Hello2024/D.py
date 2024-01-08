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
    if a.count(0) != 1:
        print('NO')
        return
    pre = [-1] + list(range(n - 1))
    nxt = list(range(1, n)) + [-1]
    ans = True
    for idx, val in sorted(zip(range(n), a), key=lambda x: x[1], reverse=True)[:-1]:
        if (pre[idx] >= 0 and 0 <= val - a[pre[idx]] <= 1) or (nxt[idx] >= 0 and 0 <= val - a[nxt[idx]] <= 1):
            if pre[idx] >= 0:
                nxt[pre[idx]] = nxt[idx]
            if nxt[idx] >= 0:
                pre[nxt[idx]] = pre[idx]
        else:
            ans = False
            break
    print("YES" if ans else "NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()