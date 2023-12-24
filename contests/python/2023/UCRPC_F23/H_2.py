import sys

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
    N, M = inlt()
    ps = []
    ps_idx = dict()
    ps_idx[0] = 0

    for i in range(N):
        val = inp()
        ps.append(val)
        ps_idx[val] = i + 1

    two_comb = dict()
    for key1 in ps_idx:
        for key2 in ps_idx:
            two_comb[key1 + key2] = [ps_idx[key1], ps_idx[key2]]

    two_sum = sorted(list(two_comb.keys()))
    k = len(two_sum)
    max_val = 0
    res = [0, 0, 0, 0]

    right = k-1
    for left in range(k):
        while right > left and two_sum[left] + two_sum[right] > M:
            right -= 1
        if two_sum[left] + two_sum[right] <= M and max_val < two_sum[left] + two_sum[right]:
            max_val = two_sum[left] + two_sum[right]
            res = two_comb[two_sum[left]] + two_comb[two_sum[right]]

    print(*res)


    # dp = dict()
    # keys = []
    # for p in ps:
    #     if p <= M and p not in dp:
    #         dp[p] = 0
    #         keys.append(p)
    #
    # for i in range(3):
    #     for j in range(len(keys)):
    #         key = keys[j]
    #         for p in ps:
    #             if key + p <= M and key + p not in dp:
    #                 dp[key + p] = key
    #                 keys.append(key + p)
    # max_key = max(dp)
    # res = []
    # for i in range(4):
    #     if max_key == 0:
    #         res.append(0)
    #     else:
    #         val = max_key - dp[max_key]
    #         max_key = dp[max_key]
    #         res.append(ps_idx[val])
    # print(*res)
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
