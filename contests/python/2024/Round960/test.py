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


from sortedcontainers import SortedList

def numberOfSubstrings(s: str) -> int:
        n = len(s)
        cur = 0
        stat = []
        for c in s:
            if c == '1':
                cur += 1
            stat.append(cur)
        zeros = collections.deque()
        zeros.appendleft(SortedList())
        max_zero = int(math.sqrt(n))

        ans = 0
        for i in range(n)[::-1]:
            for zero in range(min(len(zeros), max_zero + 1)):
                if len(zeros[zero]) == 0:
                    continue
                ans += len(zeros[zero]) - zeros[zero].bisect_left(cur + zero ** 2)
            if s[i] == '1':
                zeros[0].add(stat[i])
            else:
                zeros[0].add(stat[i])
                zeros.appendleft(SortedList())
        return ans


print(numberOfSubstrings('00011'))
