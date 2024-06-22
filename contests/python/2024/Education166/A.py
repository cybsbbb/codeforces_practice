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


lowercase_set = set('abcdefghijklmnopqrstuvwxyz')
digits_set = set('0123456789')


def solve():
    n = inp()
    s = input()[:-1]
    letter_idx = []
    letters = []
    digits_idx = []
    digits = []
    for i in range(n):
        if s[i] in lowercase_set:
            letter_idx.append(i)
            letters.append(s[i])
        elif s[i] in digits_set:
            digits_idx.append(i)
            digits.append(s[i])
        else:
            print("NO")
            return

    if (not digits_idx) or (not letter_idx) or digits_idx[-1] < letter_idx[0]:
        if sorted(letters) == letters and sorted(digits) == digits:
            print("YES")
            return
        else:
            print("NO")
            return
    else:
        print("NO")
        return
    return


t = inp()
for _ in range(t):
    solve()
