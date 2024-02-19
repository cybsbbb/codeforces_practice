import collections
import heapq
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
    s = input()[:-1]

    def helper(sub_s):
        ans = 0
        count = 0
        idx = 0
        while idx < len(sub_s):
            if sub_s[idx] == '1':
                count += 1
            else:
                if count == 0:
                    pass
                elif count % 3 == 1:
                    ans += count // 3 + 1
                    idx += 1
                elif count % 3 == 2:
                    ans += count // 3 + 1
                    idx += 0
                else:
                    ans += count // 3
                count = 0
            idx += 1

        ans += (count - 1) // 3 + 1
        # print(sub_s, ans)
        return ans

    res = 0
    for i in range(n):
        for j in range(i, n):
            res += helper(s[i: j + 1])

    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
