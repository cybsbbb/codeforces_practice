import bisect
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


def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


ps = primes(10 ** 7 + 5)
m = len(ps)
cur_cnt = 0
res = [0]

for i in range(1, m):
    if ps[i] - ps[i - 1] == 2:
        cur_cnt += 1
    res.append(cur_cnt)


def solution(ttt):
    n = inp()
    if n < 5:
        print(f"Case #{ttt}: {0}")
        return
    idx = bisect.bisect_right(ps, n)
    print(f"Case #{ttt}: {1 + res[idx - 1]}")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution(i + 1)
