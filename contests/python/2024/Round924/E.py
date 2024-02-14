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


size = 200010
dp = [float('inf')] * size
bef = [0] * size
dp[0] = 0

for i in range(1, size):
    for j in range(1, size):
        if i - j * (j + 1) // 2 < 0:
            break
        if dp[i - j * (j + 1) // 2] + j + 1 < dp[i]:
            dp[i] = dp[i - j * (j + 1) // 2] + j + 1
            bef[i] = j


def solution():
    n, x, y, s = inlt()
    remain = x % y
    x -= remain
    s -= remain * n

    if s % y != 0:
        print("NO")
        return

    ans = [x]
    s -= x
    flag = "NO"

    for i in range(n):
        if s < 0:
            break
        if dp[s // y] <= n - i - 1:
            flag = "YES"
            while len(ans) < n:
                pos = s // y
                ans.append(0)
                for j in range(bef[pos]):
                    ans.append(ans[-1] + y)
                    s -= ans[-1]
            break
        ans.append(ans[-1] + y)
        s -= ans[-1]

    print(flag)
    if flag == "YES":
        for i in range(n):
            ans[i] += remain
        print(*ans)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
