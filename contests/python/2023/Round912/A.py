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
    n, k = inlt()
    a = inlt()
    init_flag = True
    for i in range(n-1):
        if a[i] > a[i+1]:
            init_flag = False

    if init_flag == True:
        print("YES")
        return

    if init_flag == False and k == 1:
        print("NO")
        return

    print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
