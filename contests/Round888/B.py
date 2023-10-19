
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


def solution():
    n = inp()
    a = inlt()
    odd = []
    even = []
    for num in a:
        if num % 2 == 1:
            odd.append(num)
        else:
            even.append(num)
    odd.sort()
    even.sort()
    pre = -1
    odd_idx = 0
    even_idx = 0
    for num in a:
        if num % 2 == 1:
            cur_num = odd[odd_idx]
            odd_idx += 1
        else:
            cur_num = even[even_idx]
            even_idx += 1
        if cur_num < pre:
            print("NO")
            return
        else:
            pre = cur_num

    print("YES")


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
