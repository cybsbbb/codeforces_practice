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
    prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + a[i])
    remain = prefix[-1] // n
    if all(prefix[i] // i >= remain for i in range(1, n + 1)):
        print("YES")
    else:
        print("NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
