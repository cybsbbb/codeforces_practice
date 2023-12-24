import sys
input = sys.stdin.readline
sys.setrecursionlimit(1005)

n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

dp = [[None] * n for i in range(n)]


def helper(left, right):
    if dp[left][right] != None:
        return dp[left][right]

    size = (right - left + 1) if left <= right else (n - left + right + 1)
    if size <= 2:
        ans = max(A[left], A[right])
        dp[left][right] = ans
        return ans
    else:
        # take left
        res1 = A[left]
        left_sub, right_sub = left, right
        left_sub = (left_sub + 1) % n
        if A[left_sub] < A[right_sub]:
            right_sub = (right_sub + n - 1) % n
        else:
            left_sub = (left_sub + 1) % n
        res1 += helper(left_sub, right_sub)

        # take right
        res2 = A[right]
        left_sub, right_sub = left, right
        right_sub = (right_sub + n - 1) % n
        if A[left_sub] < A[right_sub]:
            right_sub = (right_sub + n - 1) % n
        else:
            left_sub = (left_sub + 1) % n
        res2 += helper(left_sub, right_sub)
        ans = max(res1, res2)
        dp[left][right] = ans
        return ans

ans = 0
for i in range(n):
    ans = max(ans, helper(i, (i - 1 + n) % n))

print(ans)
exit()

