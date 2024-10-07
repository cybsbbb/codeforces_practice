import collections
import sys
import heapq
import math

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
    s = input()[:-1]
    if n == 2:
        print(int(s))
        return

    def get_numbers(idx):
        ans = []
        for i in range(idx):
            ans.append(int(s[i]))
        ans.append(int(s[idx: idx + 2]))
        for i in range(idx + 2, n):
            ans.append(int(s[i]))
        return ans

    def calculate(numbers):
        if 0 in numbers:
            return 0
        ans = 0
        for num in numbers:
            if num == 1:
                continue
            else:
                ans += num

        if ans == 0:
            ans = 1
        return ans

    ans = float('inf')
    for idx in range(n - 1):
        numbers = get_numbers(idx)
        ans = min(ans, calculate(numbers))
    print(ans)
    return ans



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()





