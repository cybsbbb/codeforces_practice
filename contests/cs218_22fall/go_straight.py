import collections
import bisect
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


def gradient(x, y):
    if x == 0:
        return 0, 1
    if y == 0:
        return 1, 0

    gcd = math.gcd(x, y)
    x, y = x//gcd, y//gcd
    if x < 0:
        return -x, -y
    else:
        return x, y


if __name__ == '__main__':
    T = inp()
    points = []
    for i in range(T):
        x, y = inlt()
        points.append((x, y))
    n = len(points)

    res = 1
    for i in range(n):
        start = points[i]
        tmp = 0
        tmp_dict = collections.defaultdict(int)
        for j in range(n):
            end = points[j]
            if start[0] == end[0] and start[1] == end[1]:
                tmp += 1
            else:
                tmp_dict[gradient(start[0]-end[0], start[1]-end[1])] += 1
        tmp += max(tmp_dict.values())
        res = max(res, tmp)

    print(res)
