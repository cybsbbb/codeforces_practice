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

MOD = 10 ** 9 + 7



def solution():
    q = inp()
    bits_interval = [[] for _ in range(64)]
    pre_fix_sum = [0, 0, 0]

    pre_sum = 0
    for bit in range(2, 61):
        left = 1 << bit
        right = (1 << (bit + 1)) - 1
        interval = 1
        cur_val = bit
        while cur_val * bit <= left:
            interval += 1
            cur_val *= bit
        pre_sum += (min(right, cur_val * bit - 1) - left + 1) * interval
        bits_interval[bit].append((interval, cur_val))
        while cur_val * bit <= right:
            interval += 1
            cur_val *= bit
            pre_sum += (min(right, cur_val * bit - 1) - cur_val + 1) * interval
            bits_interval[bit].append((interval, cur_val))

        pre_fix_sum.append(pre_sum)

    # print(bits_interval)
    # print(pre_fix_sum)

    def query(x):
        ans = 0
        bit = 60
        while (1 << bit) & x == 0:
            bit -= 1
        ans += pre_fix_sum[bit]
        left = 1 << bit
        for interval, cur_val in bits_interval[bit]:
            if cur_val > x:
                break
            ans += (min(x, cur_val * bit - 1) - left + 1) * interval
            left = cur_val * bit
        return ans

    for _ in range(q):
        l, r = inlt()
        ans = (query(r) - query(l-1)) % MOD
        print(ans)

    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
