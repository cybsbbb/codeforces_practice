
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
    a = [0] + inlt()
    num_set = set(i for i in range(1, n + 1))
    redundent = -1
    for i in range(1, n):
        diff = a[i] - a[i-1]
        if diff not in num_set:
            redundent = diff
        else:
            num_set.remove(diff)
    if len(num_set) == 1 and redundent == -1:
        print("YES")
        return
    if len(num_set) == 2 and sum(list(num_set)) == redundent:
        print("YES")
        return

    print("NO")
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
