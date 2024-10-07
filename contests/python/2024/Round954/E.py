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
    n, k = inlt()
    a = inlt()
    stat = collections.defaultdict(list)
    for ai in sorted(a):
        stat[ai % k].append(ai)

    ans = 0
    one_flag = False
    for key, val in stat.items():
        if len(val) % 2 == 0:
            val.sort()
            for i in range(len(val) // 2):
                ans += (val[i * 2 + 1] - val[i * 2]) // k
        else:
            if one_flag is True:
                print(-1)
                return
            else:
                one_flag = True
            if len(val) == 1:
                continue
            val.sort()
            prefix = [0]
            suffix = [0]
            for i in range(len(val) // 2):
                prefix.append(prefix[-1] + (val[2 * i + 1] - val[2 * i]) // k)
            for i in range(len(val) // 2)[::-1]:
                suffix.append(suffix[-1] + (val[2 * i + 2] - val[2 * i + 1]) // k)
            prefix = prefix[1:]
            suffix = suffix[1:][::-1]
            tmp_ans = min(prefix[-1], suffix[0])
            for i in range(len(prefix) - 1):
                tmp_ans = min(tmp_ans, prefix[i] + suffix[i + 1])
            ans += tmp_ans
    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





