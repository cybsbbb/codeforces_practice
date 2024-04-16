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

n = inp()
a = inlt()

ans = 0
max_bin = ""

for i in range(1 << n):
    bin_s = bin(i)[2:].zfill(n)
    pre0 = 0
    tmp_ans = 0
    for j in range(n):
        if bin_s[j] == '1':
            tmp_ans += pre0 * pre0
            tmp_ans += a[j]
            pre0 = 0
        else:
            pre0 += 1
    tmp_ans += pre0 * pre0
    if tmp_ans > ans:
        ans = tmp_ans
        max_bin = bin_s

cache_ops = []
cache_ops.append([])
for i in range(1, 18):
    tmp = cache_ops[-1][:]
    tmp.append([0, i])
    tmp.append([0, i - 1])
    tmp.extend(cache_ops[-1])
    cache_ops.append(tmp)

ops = []
for i in range(n):
    if max_bin[i] == '0' and a[i] != 0:
        ops.append([i + 1, i + 1])

pre0 = 0
tmp_ans = 0
for j in range(n):
    if max_bin[j] == '1':
        if pre0 > 0:
            l = j - pre0 + 1
            for cl, cr in cache_ops[pre0 - 1]:
                ops.append([cl + l, cr + l])
            ops.append([l, l + pre0 - 1])
        pre0 = 0
    else:
        pre0 += 1


if pre0 > 0:
    l = n - pre0 + 1
    for cl, cr in cache_ops[pre0 - 1]:
        ops.append([cl + l, cr + l])
    ops.append([l, l + pre0 - 1])


print(ans, len(ops))
for i in range(len(ops)):
    print(*ops[i])

