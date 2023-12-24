import bisect
import collections
import sys

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
    b = inlt()
    a_flag = [False] * n

    stack_a = collections.deque()
    set_a = set()
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            return
        if a[i] == b[i]:
            a_flag[i] = True
        else:
            if b[i] in set_a:
                a_flag[i] = True
        while stack_a and stack_a[0] > b[i]:
            a_val = stack_a.popleft()
            set_a.remove(a_val)
        while stack_a and stack_a[-1] <= a[i]:
            a_val = stack_a.pop()
            set_a.remove(a_val)
        stack_a.append(a[i])
        set_a.add(a[i])

    stack_a = collections.deque()
    set_a = set()
    for i in range(n)[::-1]:
        if a[i] > b[i]:
            print("NO")
            return
        if a[i] == b[i]:
            a_flag[i] = True
        else:
            if b[i] in set_a:
                a_flag[i] = True
        while stack_a and stack_a[0] > b[i]:
            a_val = stack_a.popleft()
            set_a.remove(a_val)
        while stack_a and stack_a[-1] <= a[i]:
            a_val = stack_a.pop()
            set_a.remove(a_val)
        stack_a.append(a[i])
        set_a.add(a[i])

    if all(a_flag[i] is True for i in range(n)):
        print("YES")
    else:
        print("NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
