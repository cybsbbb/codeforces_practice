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
    s = insr()

    if n % 2 == 1:
        print(-1)
        return

    cnt = collections.Counter(s)
    cnt_values = list(cnt.values())
    if len(cnt_values) == 1:
        print(-1)
        return

    l1, l2 = cnt_values
    if abs(l1 - l2) > 1:
        print("-1")
        return

    res = []
    left = 0
    while True:
        right = len(s) - 1 - left
        if right <= left:
            break
        if s[right] != s[left]:
            left += 1
            continue
        if s[right] == s[left] and s[left] == '0':
            res.append(right + 1)
            s.insert(right + 1, '1')
            s.insert(right + 1, '0')
        elif s[right] == s[left] and s[left] == '1':
            res.append(left)
            s.insert(left, '1')
            s.insert(left, '0')
        left += 1

    if len(res) > 300:
        print(-1)
        return

    print(len(res))
    print(*res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
