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
    log = insr()
    cnt = collections.Counter()
    solved = set()
    ans = 0
    for i in range(n):
        cur_problem = log[i]
        cur_require = ord(cur_problem) - ord('A') + 1
        cnt[cur_problem] += 1
        if cnt[cur_problem] >= cur_require and cur_problem not in solved:
            ans += 1
            solved.add(cur_problem)
    print(ans)
    return 0


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
