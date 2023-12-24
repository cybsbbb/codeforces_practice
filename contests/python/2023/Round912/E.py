import sys
import heapq
import collections

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
    sx, sy = inlt()
    remaining = n
    even = []
    even_set = set()
    odd = []
    odd_set = set()
    for i in range(1, n+1):
        x, y = inlt()
        if (sx - x + sy - y) % 2 == 1:
            odd.append(i)
            odd_set.add(i)
        else:
            even.append(i)
            even_set.add(i)

    consumed = set()
    if len(even) >= len(odd):
        print("First")
        if odd:
            cur = odd.pop()
        else:
            cur = even.pop()
        consumed.add(cur)
        remaining -= 1
        print(cur)
    else:
        print("Second")
    sys.stdout.flush()

    while remaining > 1:
        # tmp = input()
        oppo = inp()
        consumed.add(oppo)
        remaining -= 1
        while odd and odd[-1] in consumed:
            odd.pop()
        while even and even[-1] in consumed:
            even.pop()
        if oppo in odd:
            if even:
                cur = even.pop()
            else:
                cur = odd.pop()
            consumed.add(cur)
            remaining -= 1
            print(cur)
        elif oppo in even:
            if odd:
                cur = odd.pop()
            else:
                cur = even.pop()
            consumed.add(cur)
            remaining -= 1
            print(cur)
        sys.stdout.flush()

    if remaining == 1:
        oppo = inp()

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
