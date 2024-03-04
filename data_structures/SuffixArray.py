from itertools import zip_longest, islice


def to_int_keys_best(l):
    """
    l: iterable of keys
    returns: a list with integer keys
    """
    seen = set()
    ls = []
    for e in l:
        if not e in seen:
            ls.append(e)
            seen.add(e)
    ls.sort()
    index = {v: i for i, v in enumerate(ls)}
    return [index[v] for v in l]


def suffix_array(s):
    """
    suffix array of s
    O(n * log(n)^2)
    """
    n = len(s)
    k = 1
    line = to_int_keys_best(s)
    while max(line) < n - 1:
        line = to_int_keys_best(
            [a * (n + 1) + b + 1
             for (a, b) in
             zip_longest(line, islice(line, k, None),
                         fillvalue=-1)])
        k <<= 1
    rk = line
    sa = [0] * n
    for i in range(n):
        sa[rk[i]] = i
    return sa, rk


def suffix_array_height(s):
    n = len(s)
    sa, rk = suffix_array(s)
    height = [0] * n
    k = 0
    for i in range(n):
        if rk[i] == 0: continue
        if k: k -= 1
        j = sa[rk[i] - 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        height[rk[i]] = k
    return sa, rk, height



s = "aabaaaab"
sa, rk, height = suffix_array_height(s)
print(sa)
print(rk)
print(height)

n = len(s)
for i in range(n):
    print(s[sa[i]:])
    print(height[i])


