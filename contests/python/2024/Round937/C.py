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
    hour = int(s[:2])
    minute = int(s[-2:])
    half = hour // 12
    hour_res = hour % 12
    hour_res = 12 if hour_res == 0 else hour_res
    print(f"{hour_res:02d}:{minute:02d} {'AM' if half == 0 else 'PM'}")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
