import sys
import collections
input = sys.stdin.readline


def solution():
    n, c = list(map(int, input().split()))
    x = sorted(list(map(int, input().split())))
    prefix_sum = [x[0]]
    for i in range(1, n):
        prefix_sum.append(x[i] + prefix_sum[-1])
    right_bound = x[-1]
    suffix_sum = [right_bound - x[-1]]
    for i in range(n - 1)[::-1]:
        suffix_sum.append((right_bound - x[i]) + suffix_sum[-1])
    suffix_sum = suffix_sum[::-1]

    def val(i, j):
        j -= 1
        mid = (i + j) // 2
        ans = 0
        ans += prefix_sum[j] - prefix_sum[mid] - (j - mid) * x[mid]
        ans += suffix_sum[i] - suffix_sum[mid] - (mid - i) * (right_bound - x[mid])
        return dp[i] + ans + c

    def insert(x, queue):
        pos = n + 1
        while queue and val(queue[-1][0], queue[-1][1]) >= val(x, queue[-1][1]):
            pos = queue[-1][1]
            queue.pop()

        if queue and val(queue[-1][0], queue[-1][2]) >= val(x, queue[-1][2]):
            l = queue[-1][1]
            r = queue[-1][2]
            while l + 1 < r:
                mid = (l + r) >> 1
                if val(x, mid) <= val(queue[-1][0], mid):
                    r = mid
                else:
                    l = mid
            queue[-1][2] = r - 1
            pos = r
        if pos != n + 1:
            queue.append([x, pos, n])
        return

    dp = [0] * (n + 1)
    op = [0] * (n + 1)
    queue = collections.deque()
    queue.append([0, 1, n])

    for i in range(1, n + 1):
        dp[i] = val(queue[0][0], i)
        op[i] = queue[0][0]
        if queue[0][2] == i:
            queue.popleft()
        if queue:
            queue[0][1] = i + 1
        insert(i, queue)
    print(dp[n])
    return


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        solution()
