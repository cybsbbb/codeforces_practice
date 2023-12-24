
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
    a, b, c, d, m = inlt()
    queue = collections.deque()
    queue.append((a, b, 0))
    seen = set()
    seen.add((a, b))
    res = -1

    while queue:
        cur_a, cur_b, cur_ops = queue.popleft()
        if cur_ops > 25:
            break
        if cur_a == c and cur_b == d:
            res = cur_ops
            break
        else:
            if (cur_a & cur_b, cur_b) not in seen:
                seen.add((cur_a & cur_b, cur_b))
                queue.append((cur_a & cur_b, cur_b, cur_ops + 1))
            if (cur_a | cur_b, cur_b) not in seen:
                seen.add((cur_a | cur_b, cur_b))
                queue.append((cur_a | cur_b, cur_b, cur_ops + 1))
            if (cur_a, cur_a ^ cur_b) not in seen:
                seen.add((cur_a, cur_a ^ cur_b))
                queue.append((cur_a, cur_a ^ cur_b, cur_ops + 1))
            if (cur_a, cur_b ^ m) not in seen:
                seen.add((cur_a, cur_b ^ m))
                queue.append((cur_a, cur_b ^ m, cur_ops + 1))
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
