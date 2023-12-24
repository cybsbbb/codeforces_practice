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


def good01String():
    n = inp()
    s = insr()

    length = 1
    segs = []
    for idx in range(1, n + 1):
        if idx < n and s[idx] == s[idx - 1]:
            length += 1
        else:
            segs.append(length)
            length = 1
    m = len(segs)

    even_num = 0
    first_odd = True
    last2 = False

    res = 0
    res_seg = 0

    for idx in range(m):
        if segs[idx] % 2 == 0:
            even_num += 1





    # for idx in range(1, n + 1):
    #     if idx < n and s[idx] == s[idx - 1]:
    #         length += 1
    #     else:
    #         res_seg += 1
    #         if length % 2 == 0:
    #             if length == 2 and not first_odd and not last2:
    #                 res_seg -= 2
    #             even_num += 1
    #             length = 1
    #         else:
    #             if first_odd:
    #                 even_num = 0
    #                 length = 1
    #                 first_odd = False
    #             else:
    #                 res += (even_num + 1)
    #                 even_num = 0
    #                 length = 1
    #                 first_odd = True
    # print(res)
    # return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        good01String()
