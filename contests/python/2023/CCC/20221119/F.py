import sys
input = sys.stdin.readline
def inp():
    return(int(input()))


def cake_cutting(n, cakes):
    if n <= 2:
        return max(cakes)
    res = 0
    takes = dict()
    for first_take in range(n):
        new_cakes = cakes[first_take + 1:] + cakes[:first_take]
        if new_cakes[0] < new_cakes[-1]:
            new_cakes.pop(-1)
            take = ((first_take - 1) % n, first_take)
        else:
            new_cakes.pop(0)
            take = (first_take, (first_take + 1) % n)
        if take in takes:
            res = max(res, takes[take] + cakes[take[0]])
            res = max(res, takes[take] + cakes[take[1]])
            continue

        dp = [[0] * (n - 2) for _ in range(n - 2)]
        # Celvin takes the last one
        if n % 2 == 0:
            for length in range(1, n - 2, 2):
                for start in range(0, n - length - 2):
                    end = start + length
                    # Celvin takes the last one
                    if length == 1:
                        dp[start][end] = max(new_cakes[start], new_cakes[end])
                    else:
                        # take left
                        if new_cakes[start + 1] > new_cakes[end]:
                            tmp_left = dp[start + 2][end] + new_cakes[start]
                        else:
                            tmp_left = dp[start + 1][end - 1] + new_cakes[start]
                        # take right
                        if new_cakes[start] > new_cakes[end - 1]:
                            tmp_right = dp[start + 1][end - 1] + new_cakes[end]
                        else:
                            tmp_right = dp[start][end - 2] + new_cakes[end]
                        dp[start][end] = max(tmp_left, tmp_right)
        # Preston takes the last one
        elif n % 2 == 1:
            for length in range(0, n - 2, 2):
                for start in range(0, n - length - 2):
                    end = start + length
                    # Preston takes the last one
                    if length == 0:
                        dp[start][end] = max(new_cakes[start], new_cakes[end])
                    else:
                        # take left
                        if new_cakes[start + 1] > new_cakes[end]:
                            tmp_left = dp[start + 2][end] + new_cakes[start]
                        else:
                            tmp_left = dp[start + 1][end - 1] + new_cakes[start]
                        # take right
                        if new_cakes[start] > new_cakes[end - 1]:
                            tmp_right = dp[start + 1][end - 1] + new_cakes[end]
                        else:
                            tmp_right = dp[start][end - 2] + new_cakes[end]
                        dp[start][end] = max(tmp_left, tmp_right)
        takes[take] = dp[0][-1]
        res = max(res, dp[0][-1] + cakes[first_take])
    return res


if __name__ == '__main__':
    n = inp()
    cakes = []
    for i in range(n):
        cakes.append(inp())

    print(cake_cutting(n, cakes))
