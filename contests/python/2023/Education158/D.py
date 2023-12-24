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
    left = [a[0]]
    right = [a[-1]]
    for i in range(1, n):
        left.append(max(left[-1] + 1, a[i]))
    for i in range(n-1)[::-1]:
        right.append(max(right[-1] + 1, a[i]))
    right = right[::-1]
    ans = min(left[-1], right[0])
    for i in range(1, n - 1):
        left_require = left[i - 1]
        left_num = i
        right_require = right[i + 1]
        right_num = n - 1 - i
        tmp_ans = max(left_require + right_num + 1, right_require + left_num + 1, a[i])
        ans = min(ans, tmp_ans)

    print(ans)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
