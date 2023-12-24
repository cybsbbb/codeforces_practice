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


def is_good(s, n):
    for i in range(n-1):
        if s[i] == s[i+1]:
            return False
    return True


def solution():
    n, m = inlt()
    s = insr()
    t = insr()

    if is_good(s, n) is True:
        print("Yes")
        return

    if is_good(t, m) is False:
        print("No")
        return

    flag00 = False
    flag11 = False

    for i in range(n-1):
        if s[i] == s[i + 1] and s[i] == '0':
            flag00 = True
        if s[i] == s[i + 1] and s[i] == '1':
            flag11 = True

    if flag00 is True and flag11 is True:
        print("No")
        return

    if flag00 is True and t[0] == '1' and t[-1] == '1':
        print("Yes")
        return

    if flag11 is True and t[0] == '0' and t[-1] == '0':
        print("Yes")
        return

    print("No")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
