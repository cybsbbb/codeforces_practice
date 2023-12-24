import sys

# input = sys.stdin.buffer.readline
input = sys.stdin.readline

from math import gcd


for _ in range(int(input())):
    n, k = map(int, input().split())

    a = list(map(int, input().split()))

    ones = []
    twos = []

    ans = 0

    i = 0
    while i < n:
        j = i
        while j < n and (a[i] == 1) == (a[j] == 1):
            j += 1

        if a[i] == 1:
            if i != 0 and j != n:
                ones.append(j-i)
            ans += j-i+1 - (i==0) - (j==n)  # gcd == 1 and a[i] == 1 or a[i+1] == 1
        else:
            twos.append([i, j-1])

        i = j

    if len(twos) == 0:
        ans -= (k-1)
    else:
        sub2 = 0

        for s, e in twos:
            g = [gcd(a[i], a[i+1]) == 1 for i in range(s, e)]

            ans += sum(g)  # gcd == 1 and not (a[i] == 1 or a[i+1] == 1)

            i = 0
            while i < len(g):
                j = i
                while j < len(g) and g[i] == g[j]:
                    j += 1

                if g[i] == 1:
                    sub2 += (j - i) // 2

                i = j

        ones.sort()

        # Make a[i] = 0 where a[i-1], a[i], a[i+1] all > 1 => remove 2 sad
        sub = min(sub2, k)
        k -= sub
        ans -= 2 * sub

        # Removing from one end => -1, -1, ... -2 sad
        for x in ones:
            if k >= x:
                k -= x
                ans -= x+1

        ans -= min(ans, k)

    print(ans)
