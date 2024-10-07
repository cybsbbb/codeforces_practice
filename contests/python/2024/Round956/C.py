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
    n = inp()
    a = inlt()
    b = inlt()
    c = inlt()
    tot = sum(a)
    threshold = (tot + 2) // 3
    prefix_a = [0]
    prefix_b = [0]
    prefix_c = [0]
    for i in range(n):
        prefix_a.append(prefix_a[-1] + a[i])
        prefix_b.append(prefix_b[-1] + b[i])
        prefix_c.append(prefix_c[-1] + c[i])

    status = 7
    ans = [-1] * 6

    def helper(cur_idx, status, ans):
        if status == 1:
            a_prefix = prefix_a[n] - prefix_a[cur_idx]
            if a_prefix >= threshold:
                ans[0] = cur_idx + 1
                ans[1] = n
                return ans
            else:
                return False
        if status == 2:
            b_prefix = prefix_b[n] - prefix_b[cur_idx]
            if b_prefix >= threshold:
                ans[2] = cur_idx + 1
                ans[3] = n
                return ans
            else:
                return False
        if status == 4:
            c_prefix = prefix_c[n] - prefix_c[cur_idx]
            if c_prefix >= threshold:
                ans[4] = cur_idx + 1
                ans[5] = n
                return ans
            else:
                return False

        if status & 1:
            for i in range(cur_idx, n):
                a_prefix = prefix_a[i + 1] - prefix_a[cur_idx]
                if a_prefix >= threshold:
                    ans[0] = cur_idx + 1
                    ans[1] = i + 1
                    if helper(i + 1, status ^ 1, ans):
                        return ans
                    ans[0] = 0
                    ans[1] = 0
                    break

        if status & 2:
            for i in range(cur_idx, n):
                b_prefix = prefix_b[i + 1] - prefix_b[cur_idx]
                if b_prefix >= threshold:
                    ans[2] = cur_idx + 1
                    ans[3] = i + 1
                    if helper(i + 1, status ^ 2, ans):
                        return ans
                    ans[2] = 0
                    ans[3] = 0
                    break

        if status & 4:
            for i in range(cur_idx, n):
                c_prefix = prefix_c[i + 1] - prefix_c[cur_idx]
                if c_prefix >= threshold:
                    ans[4] = cur_idx + 1
                    ans[5] = i + 1
                    if helper(i + 1, status ^ 4, ans):
                        return ans
                    ans[4] = 0
                    ans[5] = 0
                    break

        return False

    ans = helper(0, 7, ans)

    if not ans:
        print(-1)
    else:
        print(*ans)

    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





