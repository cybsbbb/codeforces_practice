import sys
import math
import collections

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


def halfaresame(n, numbers):
    counter = collections.Counter(numbers)
    numbers_distinct = sorted(counter.keys())
    key, value = counter.most_common(1)[0]
    if value >= n // 2:
        print("-1")
        return -1
    ret = 1
    for i in range(len(numbers_distinct)):
        stat = collections.defaultdict(int)
        for j in range(i+1, len(numbers_distinct)):
            diff = numbers_distinct[j] - numbers_distinct[i]
            for k in range(1, int(math.sqrt(diff)+1)):
                if diff % k == 0:
                    stat[k] += counter[numbers_distinct[j]]
                    if (diff // k) != k:
                        stat[diff // k] += counter[numbers_distinct[j]]
        for key in stat:
            if stat[key] + counter[numbers_distinct[i]] >= n // 2:
                ret = max(ret, key)
    print(ret)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        n = inp()
        numbers = inlt()
        halfaresame(n, numbers)
