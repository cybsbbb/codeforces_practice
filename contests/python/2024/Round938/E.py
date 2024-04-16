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
    s = list(map(int, input()[:-1]))

    def helper(cur_len):
        q = collections.deque()
        for i in range(n):
            while q and q[0] < i:
                q.popleft()
            cur_val = s[i] ^ 1 if len(q) % 2 == 1 else s[i]
            if cur_val == 0:
                if i > n - cur_len:
                    return False
                else:
                    q.append(i + cur_len - 1)
        return True

    ans = 1
    for cur_len in range(2, n + 1)[::-1]:
        if helper(cur_len):
            ans = cur_len
            break

    print(ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
