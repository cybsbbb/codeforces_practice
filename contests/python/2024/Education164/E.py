import sys
from itertools import accumulate

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


n = inp()
a = inlt()
mx = max(a)
ans = [0] * (mx + 1)
f = [0] * (mx + 1)
f[a[0]] += 1

for i in range(1, n):
    f[a[i]] += 1
    f[min(a[i - 1], a[i])] -= 1

f = list(accumulate(f))

for k in range(1, mx + 1):
    for i in range(1, (mx - 1) // k + 2):
        ans[k] += (f[min(mx, i * k)] - f[(i - 1) * k]) * i

print(*ans[1:])


