t = int(input())
for _ in range(t):
    l, n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [list(map(int, input().split())) for _ in range(n)]
    max_num = 7  # Since numbers are up to 7

    # Preprocess positions for each number
    positions = [[] for _ in range(max_num + 1)]
    for r in range(n):
        for c in range(m):
            positions[b[r][c]].append((r + 1, c + 1))  # 1-based indexing

    # Sort positions for each number
    for x in range(1, max_num + 1):
        positions[x].sort()

    # Initialize DP table
    dp = [[[False] * (l + 2) for _ in range(m + 2)] for _ in range(n + 2)]
    # Base case
    for r in range(n + 1):
        for c in range(m + 1):
            dp[r][c][l + 1] = False  # Beyond the last index, player loses

    # Fill DP table
    for i in range(l, 0, -1):
        x = a[i - 1]
        pos_list = positions[x]
        for r in range(n, 0, -1):
            for c in range(m, 0, -1):
                dp[r][c][i] = False
                # Find positions where r' >= r and c' >= c
                left = 0
                right = len(pos_list) - 1
                idx = len(pos_list)
                while left <= right:
                    mid = (left + right) // 2
                    if pos_list[mid][0] >= r and pos_list[mid][1] >= c:
                        idx = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                # Check possible moves
                for k in range(idx, len(pos_list)):
                    r1, c1 = pos_list[k]
                    if r1 >= r and c1 >= c:
                        if not dp[r1 + 1][c1 + 1][i + 1]:
                            dp[r][c][i] = True
                            break
                    else:
                        break  # Since positions are sorted, no need to check further

    # Determine the winner
    winner = "T" if dp[1][1][1] else "N"
    print(winner)
