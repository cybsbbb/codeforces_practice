MOD = 998244353


def solve(n, arr):
    res = 0
    for bit in range(31):
        odd_cnt = 0
        odd_tot_len = 0
        even_cnt = 0
        even_tot_len = 0
        ones_cnt = 0

        target_tot_len = 0
        for i in range(n):
            if ((arr[i] >> bit) & 1):
                ones_cnt += 1
            if ones_cnt % 2 == 0:
                even_cnt += 1
                even_tot_len += (i + 1)
                target_tot_len += (i + 1) * odd_cnt - odd_tot_len
            else:
                odd_cnt += 1
                odd_tot_len += (i + 1)
                target_tot_len += (i + 1) * even_cnt - even_tot_len + (i + 1)

        res = (res + (1 << bit) * target_tot_len) % MOD
    return res


n = int(input().strip())
arr = list(map(int, input().strip().split()))

print(solve(n, arr))
