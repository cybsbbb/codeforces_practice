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


MOD = 998244353
factorial = [1]
for i in range(1, 2000020):
    factorial.append(factorial[-1] * i % MOD)


def comb(n, m):
    if m < 0:
        return 1
    return factorial[n] * pow(factorial[n - m], MOD-2, MOD) * pow(factorial[m], MOD-2, MOD) % MOD


def solution():
    c1, c2, c3, c4 = inlt()
    if abs(c1 - c2) > 1:
        print(0)
        return

    if c1 == 0 and c2 == 0:
        if c3 == 0 or c4 == 0:
            print(1)
        else:
            print(0)
        return

    if c1 == c2:
        choice = c1
        ans = comb(c3 + choice - 1, choice - 1) * comb(c4 + choice, choice) + comb(c4 + choice - 1, choice - 1) * comb(c3 + choice, choice)
        ans %= MOD
    else:
        choice = (c1 + c2 + 1) // 2
        ans = comb(c3 + choice - 1, choice - 1) * comb(c4 + choice - 1, choice - 1)
        ans %= MOD

    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
