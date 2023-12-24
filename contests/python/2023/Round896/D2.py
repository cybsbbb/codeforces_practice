import collections
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
    a = inlt()
    sum_a = sum(a)
    if sum_a % n != 0:
        print("No")
        return
    average = sum_a // n
    count = collections.Counter()
    average_cnt = 0
    singles = []
    for candy in a:
        if candy == average:
            average_cnt += 1
        diff = abs(candy - average)
        if bin(diff)[2:].count('1') == 1:
            if candy > average:
                singles.append((diff, -1))
            else:
                singles.append((diff, 1))
        else:
            less = diff & (-diff)
            large = diff + less
            if bin(large)[2:].count('1') > 1:
                print("No")
                return
            if candy > average:
                count[large] -= 1
                count[less] += 1
            else:
                count[large] += 1
                count[less] -= 1

    for diff, indicate in sorted(singles, reverse=True):
        if count[2 * diff] * indicate < 0:
            count[2 * diff] += indicate
            count[diff] += -indicate
        else:
            count[diff] += indicate

    negative_cnt = 0
    positive_cnt = 0
    for key in count:
        if count[key] < 0:
            negative_cnt += count[key]
        if count[key] > 0:
            positive_cnt += count[key]

    if negative_cnt == 0 and positive_cnt == 0:
        print("Yes")
        return

    print("No")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
