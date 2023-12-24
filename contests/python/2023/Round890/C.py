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
    res = max(a)
    # From end to begin
    for start in range(n-1, 0, -1):
        remaining = k
        cur_height = a[start]
        res = max(res, cur_height)
        cur_position = start
        while cur_position > 0:
            if a[cur_position-1] <= (cur_height + 1) and cur_height + 1 - a[cur_position-1] <= remaining:
                remaining -= (cur_height + 1 - a[cur_position-1])
                cur_height += 1
                cur_position -= 1
                res = max(res, cur_height)
            else:
                break
    # From begin to end
    for start in range(0, n-1):
        start_height = a[start]
        remaining = k
        cur_height = a[start]
        cur_position = start
        while cur_position < n-1:
            if a[cur_position + 1] <= (cur_height - 1):
                if cur_height - 1 - a[cur_position + 1] <= remaining:
                    remaining -= (cur_height - 1 - a[cur_position + 1])
                    cur_height -= 1
                    cur_position += 1
                else:
                    break
            else:
                inteval_length = cur_position - start + 1
                max_increase_height = a[cur_position + 1] - (cur_height - 1)
                if inteval_length * max_increase_height <= remaining:
                    remaining -= inteval_length * max_increase_height
                    start_height += max_increase_height
                    cur_height = cur_height - 1 + max_increase_height
                    cur_position += 1
                    res = max(res, start_height)
                else:
                    increased_height = remaining // inteval_length
                    start_height += increased_height
                    res = max(res, start_height)
                    break

    print(res)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
