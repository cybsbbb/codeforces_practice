import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        l, n, m = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

        dp_current = [[False] * (m + 1) for _ in range(n + 1)]
        dp_next = [[False] * (m + 1) for _ in range(n + 1)]

        # Process DP from i = l - 1 down to 0
        for i in range(l - 1, -1, -1):
            dp_current, dp_next = dp_next, dp_current  # Swap dp_current and dp_next
            x = a[i]
            for r in range(n - 1, -1, -1):
                for c in range(m - 1, -1, -1):
                    if b[r][c] == x and not dp_next[r + 1][c + 1]:
                        dp_current[r][c] = True
                    else:
                        dp_current[r][c] = dp_current[r + 1][c] or dp_current[r][c + 1]

        # Determine the winner
        winner = "T" if dp_current[0][0] else "N"
        print(winner)

main()

