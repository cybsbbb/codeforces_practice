import collections
import sys
import heapq
import math

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
    a, b, n, m = inlt()

    points = []
    for i in range(n):
        xi, yi = inlt()
        xi -= 1
        yi -= 1
        points.append([xi, yi, i])
    col_deque = collections.deque(sorted(points, key=lambda x: x[0]))
    row_deuqe = collections.deque(sorted(points, key=lambda x: x[1]))
    removed = set()
    x_min, x_max, y_min, y_max = 0, a - 1, 0, b - 1
    ans = []
    for _ in range(m):
        c, k = input()[:-1].split()
        k = int(k)
        tmp_ans = 0
        if c == 'U':
            x_min += k
            while col_deque and col_deque[0][0] < x_min:
                _, _, idx = col_deque.popleft()
                if idx not in removed:
                    tmp_ans += 1
                    removed.add(idx)
        elif c == 'D':
            x_max -= k
            while col_deque and col_deque[-1][0] > x_max:
                _, _, idx = col_deque.pop()
                if idx not in removed:
                    tmp_ans += 1
                    removed.add(idx)
        elif c == 'L':
            y_min += k
            while row_deuqe and row_deuqe[0][1] < y_min:
                _, _, idx = row_deuqe.popleft()
                if idx not in removed:
                    tmp_ans += 1
                    removed.add(idx)
        elif c == 'R':
            y_max -= k
            while row_deuqe and row_deuqe[-1][1] > y_max:
                _, _, idx = row_deuqe.pop()
                if idx not in removed:
                    tmp_ans += 1
                    removed.add(idx)
        ans.append(tmp_ans)

    alice = sum(ans[i] for i in range(0, len(ans), 2))
    bob = sum(ans[i] for i in range(1, len(ans), 2))
    print(alice, bob)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





