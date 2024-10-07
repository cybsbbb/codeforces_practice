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


MOD = 998244353

def solution(ttt):
    n = inp()
    # s = []
    # max_length = 0
    trie = dict()
    for _ in range(n):
        trie_tmp = trie
        si = input()[:-1]
        # s.append(si)
        # max_length = max(max_length, len(si))
        for c in si:
            if c not in trie_tmp:
                trie_tmp[c] = dict()
            trie_tmp = trie_tmp[c]

    queue = collections.deque((trie, 1))
    ans = 0
    while queue:
        cur_trie, cur_cnt = queue.popleft()
        ans += cur_cnt







    # dp_cur = [0] * 26
    # for i in range(n):
    #     if s[i][0] == '?':
    #         for j in range(26):
    #             dp_cur[j] = 1
    #         break
    #     else:
    #         dp_cur[ord(s[i][0]) - ord('A')] = 1
    # ans = sum(dp_cur) + 1





if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution(i + 1)
