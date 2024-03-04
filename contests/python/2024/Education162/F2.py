import sys, os, io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

input = sys.stdin.readline

def binary_search(c1, c2):
    m = (c1 + c2 + 1) // 2
    while abs(c1 - c2) > 1:
        m = (c1 + c2 + 1) // 2
        if ok(m):
            c2 = m
        else:
            c1 = m
    m = max(m - 1, u)
    while not ok(m):
        m += 1
    return m

def ok(m):
    if m < u:
        return False
    elif m >= n:
        return True
    for i in range(n - m + 1):
        if u - (c[i + m] - c[i]) <= k:
            return True
    return False

def suffix_array(s):
    b = (len(s) - 1).bit_length()
    u = s + [0] * ((1 << b) - len(s))
    l, j = len(u) - 1, 1
    v, w = [0] * (l + 1), [0] * (l + 1)
    for _ in range(b):
        m = max(u)
        s0 = [0] * (m + 3)
        for i in u:
            s0[i + 2] += 1
        for i in range(1, m + 3):
            s0[i] += s0[i - 1]
        for i in range(l + 1):
            k = u[i] + 1
            v[s0[k]] = i - j
            s0[k] += 1
        for i in v:
            k = u[i]
            w[s0[k]] = i
            s0[k] += 1
        c, la1, la2 = 0, 0, 0
        for i in w:
            x, y = u[i], u[(i + j) & l]
            if la1 ^ x or la2 ^ y:
                la1, la2 = x, y
                c += 1
            v[i] = c
        u, v = v, u
        if c == l + 1:
            break
        j <<= 1
    l = u[-1]
    sa = [0] * len(s)
    for i in range(len(s) - 1):
        sa[u[i] - l] = i
    sa[0] = len(sa) - 1
    return sa

n, k = map(int, input().split())
mod = pow(10, 9) + 7
s = list(input().rstrip())
s = [i & 1 for i in s]
a, k0, r = list(s), k, n - 1
for l in range(n):
    if not l < r or not k0:
        break
    if a[l]:
        while l < r and a[r]:
            r -= 1
        if l < r:
            a[l], a[r] = a[r], a[l]
            k0 -= 1
inf = pow(10, 9) + 1
f = 0
for i in range(n - 1):
    if a[i] > a[i + 1]:
        f = 1
        break
if f:
    k -= 1
    s.reverse()
    c = [0] * (n + 1)
    for i in range(n):
        c[i + 1] = s[i] + c[i]
    u = c[n]
    l = binary_search(0, n + 1)
    v = [inf] * n
    if not s[-1]:
        v[-1] = 0
    for i in range(n - 2, -1, -1):
        v[i] = (v[i + 1] + 1) * s[i]
    mi = inf
    for i in range(n - l + 1):
        if u - (c[i + l] - c[i]) == k:
            mi = min(mi, v[i])
    p = [0] * n
    for i in range(n - l + 1):
        if u - (c[i + l] - c[i]) == k and mi == v[i]:
            p[i] = 1
    y = []
    for i in range(n):
        if not s[i]:
            y.append(i)
    z = [0] * len(y)
    for i in range(len(z) - 1):
        z[i] = y[i + 1] - y[i]
    sa = suffix_array(z)
    for i in sa:
        if p[y[i] - mi]:
            l0, r0 = y[i] - mi, y[i] - mi + l
            break
    y, k0 = s[l0:r0], k
    for i in range(l - 1, -1, -1):
        if not k0:
            break
        if not y[i]:
            y[i] = 1
            k0 -= 1
    b = [0] * (n - l) + y
    for i in range(n):
        if a[i] < b[i]:
            break
        elif a[i] > b[i]:
            a = b
            break
ans, p = 0, 1
for i in a[::-1]:
    ans += i * p
    p = 2 * p % mod
ans %= mod
print(ans)

