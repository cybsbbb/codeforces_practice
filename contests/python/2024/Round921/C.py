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
    n, k, m = inlt()
    s = insr()
    cur_set = set()
    cur_length = 0
    ans = []
    for c in s:
        cur_set.add(c)
        if len(cur_set) == k:
            ans.append(c)
            cur_length += 1
            cur_set.clear()
    if cur_length >= n:
        print("YES")
        return
    for i in range(k):
        if chr(ord('a') + i) not in cur_set:
            ans.append(chr(ord('a') + i))
            break

    ans += ['a'] * (n - len(ans))
    print("NO")
    print("".join(ans))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
