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
    s = input()[:-1]
    words = s.split(' ')
    res = []
    if len(words) == 3:
        if ord('a') <= ord(words[2][0]) <= ord('z'):
            res.append(chr(ord(words[2][0]) + ord('A') - ord('a')) + words[2][1:-1])
        else:
            res.append(words[2][0] + words[2][1:-1])
    else:
        if ord('a') <= ord(words[2][0]) <= ord('z'):
            res.append(chr(ord(words[2][0]) + ord('A') - ord('a')) + words[2][1:])
        else:
            res.append(words[2][0] + words[2][1:])
        for i in range(3, len(words)-1):
            res.append(words[i])
        res.append(words[-1][:-1])
    res.append(words[1])
    res.append(words[0] + '.')
    print(' '.join(res))
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
