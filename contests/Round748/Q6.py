import sys
import math
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


def gardenerAndTree(n, k):
    tree = collections.defaultdict(list)
    layer = [0] * n
    rem = [0] * n
    for i in range(n - 1):
        a, b = inlt()
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
        rem[a - 1] += 1
        rem[b - 1] += 1

    q = collections.deque()

    for i in range(n):
        if rem[i] == 1:
            q.append(i)
            layer[i] = 1

    while len(q) > 0:
        front = q.popleft()
        for v in tree[front]:
            if rem[v] != 1:
                rem[v] -= 1
                if rem[v] == 1:
                    layer[v] = layer[front] + 1
                    q.append(v)

    ret = 0
    for i in range(n):
        if layer[i] > k:
            ret += 1
    print(ret)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        input()
        n, k = inlt()
        gardenerAndTree(n, k)
