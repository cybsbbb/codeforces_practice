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

MOD = 998244353

def solution():
    n = inp()
    a = inlt()
    stack = []
    dp = [0 for _ in range(n + 1)]
    dp_prefix_sum = [0 for _ in range(n + 1)]
    stack_sum = 0
    for i in range(n):
        while stack and a[stack[-1]] > a[i]:
            stack_sum -= dp[stack[-1]]
            stack.pop()
        j = stack[-1] + 1 if stack else 0
        dp[i] = (stack_sum + dp_prefix_sum[i] - dp_prefix_sum[j] + (1 if not stack else 0)) % MOD
        dp_prefix_sum[i + 1] = (dp_prefix_sum[i] + dp[i]) % MOD
        stack_sum = (stack_sum + dp[i]) % MOD
        stack.append(i)
    print(stack_sum % MOD)
    return 0


if __name__ == '__main__':
    t = inp()
    for _ in range(t):
        solution()
