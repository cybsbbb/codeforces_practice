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


def solve():
    n, m = inlt()
    a = inlt()
    b = inlt()
    programmer_prefer = []
    tester_prefer = []
    for i in range(n + m + 1):
        if a[i] > b[i]:
            programmer_prefer.append(i)
        else:
            tester_prefer.append(i)

    programmer_prefer_prefix = [0]
    for i in programmer_prefer:
        programmer_prefer_prefix.append(programmer_prefer_prefix[-1] + a[i])
    programmer_prefer_suffix = [0]
    for i in programmer_prefer[::-1]:
        programmer_prefer_suffix.append(programmer_prefer_suffix[-1] + b[i])
    programmer_prefer_suffix = programmer_prefer_suffix[::-1]

    tester_prefer_prefix = [0]
    for i in tester_prefer:
        tester_prefer_prefix.append(tester_prefer_prefix[-1] + b[i])
    tester_prefer_suffix = [0]
    for i in tester_prefer[::-1]:
        tester_prefer_suffix.append(tester_prefer_suffix[-1] + a[i])
    tester_prefer_suffix = tester_prefer_suffix[::-1]

    ans = []
    for i in range(n + m + 1):
        # programmer
        if a[i] > b[i]:
            if len(programmer_prefer) - 1 >= n:
                res = tester_prefer_prefix[-1]
                if n == 0 or programmer_prefer[n - 1] < i:
                    res += programmer_prefer_prefix[n] + programmer_prefer_suffix[n] - b[i]
                else:
                    res += programmer_prefer_prefix[n + 1] + programmer_prefer_suffix[n + 1] - a[i]
            else:
                res = programmer_prefer_prefix[-1] - a[i]
                res += tester_prefer_prefix[m] + tester_prefer_suffix[m]
            ans.append(res)
        elif a[i] < b[i]:
            if len(tester_prefer) - 1 >= m:
                res = programmer_prefer_prefix[-1]
                if m == 0 or tester_prefer[m - 1] < i:
                    res += tester_prefer_prefix[m] + tester_prefer_suffix[m] - a[i]
                else:
                    res += tester_prefer_prefix[m + 1] + tester_prefer_suffix[m + 1] - b[i]
            else:
                res = tester_prefer_prefix[-1] - b[i]
                res += programmer_prefer_prefix[n] + programmer_prefer_suffix[n]
            ans.append(res)

    print(*ans)
    return



t = inp()
for _ in range(t):
    solve()
