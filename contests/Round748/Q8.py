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


def changingBrackets():
    str = insr()
    n = inp()

    odd = [0] * (len(str)+1)
    even = [0] * (len(str)+1)

    for i in range(len(str)):
        odd[i + 1] = odd[i]
        even[i + 1] = even[i]
        if str[i] == '[' or str[i] == ']':
            if (i + 1) % 2 == 1:
                odd[i + 1] += 1
            else:
                even[i + 1] += 1

    for _ in range(n):
        l, r = inlt()
        odd_sub = odd[r] - odd[l-1]
        even_sub = even[r] - even[l-1]
        print(abs(odd_sub - even_sub))
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        changingBrackets()
