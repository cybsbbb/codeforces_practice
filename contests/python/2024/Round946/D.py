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
    s = input()[:-1]
    r = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
    cnt = collections.Counter(s)
    if (cnt['N'] + cnt['S']) % 2 != 0:
        print("NO")
        return
    else:
        if cnt['N'] % 2 == 1:
            r['N'] += 1 + cnt['N'] // 2
            r['S'] += 1 + cnt['S'] // 2
        else:
            r['N'] += cnt['N'] // 2
            r['S'] += cnt['S'] // 2

    if (cnt['E'] + cnt['W']) % 2 != 0:
        print("NO")
        return
    else:
        r['E'] += cnt['E'] // 2
        r['W'] += cnt['W'] // 2
    ans = []
    for c in s:
        if r[c] > 0:
            ans.append('R')
            r[c] -= 1
        else:
            ans.append('H')

    if len(set(ans)) == 1:
        print("NO")
    else:
        print(''.join(ans))

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
