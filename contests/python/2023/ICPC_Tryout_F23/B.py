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
    peoples = collections.defaultdict(int)
    for i in range(n):
        start, duration = inlt()
        peoples[start] += 1
        peoples[start + duration] -= 1
    days = sorted(list(peoples.keys()))
    res = [0] * (n + 1)
    cur_people = peoples[days[0]]
    for i in range(1, len(days)):
        res[cur_people] += days[i] - days[i-1]
        cur_people += peoples[days[i]]
    print(*res[1:])
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
