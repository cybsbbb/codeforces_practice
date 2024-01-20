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
    a = insr()
    b = insr()
    c = insr()
    flag = False
    for i in range(n):
        if a[i] == b[i]:
            if c[i] != a[i]:
                flag = True
                break
            else:
                pass
        elif a[i] != b[i]:
            if c[i] != a[i] and c[i] != b[i]:
                flag = True
                break

    print("YES" if flag else "NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
