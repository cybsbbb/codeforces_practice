MOD = 10 ** 9 + 7
MAXN = 2 * 10 ** 5 + 5

fac = [1] * MAXN
inv_fac = [1] * MAXN

for i in range(1, MAXN):
    fac[i] = fac[i - 1] * i % MOD
inv_fac[MAXN - 1] = pow(fac[MAXN - 1], -1, MOD)
for i in range(MAXN - 2, -1, -1):
    inv_fac[i] = inv_fac[i + 1] * (i + 1) % MOD


def combination(n, k):
    return (fac[n] * inv_fac[k] % MOD) * inv_fac[n - k] % MOD


def permutation(n, k):
    return fac[n] * inv_fac[n - k] % MOD
