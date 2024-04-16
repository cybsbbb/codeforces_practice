import sys
import collections
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


MOD = 10 ** 9 + 7
N = 10 ** 6 + 5

pows = [1]
for i in range(N):
    pows.append(pows[-1] * 233 % MOD)

inv = pow(233, -1, MOD)
pows_neg = [1]
for i in range(N):
    pows_neg.append(pows_neg[-1] * inv % MOD)


def solution():
    s = input()[:-1]
    n = len(s)

    if s != s[::-1]:
        print("YES")
        print(1)
        print(s)
        return

    forward = [0]
    for c in s:
        forward.append((forward[-1] * 233 + ord(c) - ord('a')) % MOD)
    forward = forward[1:]

    backward = [0]
    for c in s[::-1]:
        backward.append((backward[-1] * 233 + ord(c) - ord('a')) % MOD)
    backward = backward[1:][::-1]

    for i in range(n - 1):
        left_forward = forward[i]
        left_backward = (backward[0] - backward[i + 1]) * pows_neg[n - i - 1] % MOD
        right_forward = (forward[-1] - forward[i]) * pows_neg[i + 1] % MOD
        right_backward = backward[i + 1]
        if left_forward != left_backward and right_forward != right_backward:
            print("YES")
            print(2)
            print(s[:i + 1], s[i + 1:])
            return

    print("NO")
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
