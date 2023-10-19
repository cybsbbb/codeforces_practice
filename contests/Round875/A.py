t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a_idx_sorted = sorted([(a_val, a_idx) for a_idx, a_val in enumerate(a)])

    b = [0] * n

    for i in range(n):
        b[i] = a_idx_sorted[~(a[i]-1)][0]

    print(' '.join(map(str, b)))
