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
    if n == 1:
        print(0)
        return
    ans = 0
    ans_list = []
    max_a, min_a = max(a), min(a)
    while max_a != min_a:
        x = 0 if min_a % 2 == 0 else 1
        ans_list.append(x)
        min_a = (min_a + x) // 2
        max_a = (max_a + x) // 2
        ans += 1
    print(ans)
    if len(ans_list) <= n:
        print(*ans_list)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
