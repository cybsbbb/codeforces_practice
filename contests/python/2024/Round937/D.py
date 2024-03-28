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


divisors = [int(bin(i)[2:]) for i in range(2, 33)]



def solution():
    n = inp()

    def helper(cur):
        if cur == 1:
            return True
        res = False
        for divisor in divisors:
            if divisor > cur:
                break
            if cur % divisor == 0:
                res = res | helper(cur // divisor)
            if res is True:
                break
        return res

    print("YES" if helper(n) else "NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
