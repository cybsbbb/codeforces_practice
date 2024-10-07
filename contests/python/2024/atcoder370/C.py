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


s = input()[:-1]
t = input()[:-1]

n = len(s)

small = []
large = []

for i in range(n):
    if s[i] != t[i]:
        if s[i] > t[i]:
            small.append(i)
        else:
            large.append(i)

s_list = list(s)

print(len(small) + len(large))

for i in small:
    s_list[i] = t[i]
    print(''.join(s_list))

for i in large[::-1]:
    s_list[i] = t[i]
    print(''.join(s_list))
