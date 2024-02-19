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


for i in range(inp()):
    n = inp()
    s = input()[:-1]
    prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + ord(s[i]) - ord('0'))
    prefix = prefix[1:][::-1]

    while prefix[-1] == 0:
        prefix.pop()

    for i in range(len(prefix) - 1):
        prefix[i + 1] += prefix[i] // 10
        prefix[i] %= 10

    while prefix[-1] >= 10:
        prefix.append(prefix[-1] // 10)
        prefix[-2] %= 10

    print(''.join(map(str, prefix[::-1])))
