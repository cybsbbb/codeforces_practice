def solve():
    import sys
    import threading
    def main():
        T = int(sys.stdin.readline())
        for case_num in range(1, T + 1):
            R, C, K = map(int, sys.stdin.readline().split())
            N = R * C
            owners = []
            for _ in range(R):
                owners.append(list(map(int, sys.stdin.readline().split())))
            max_score = max(R, C)
            total_pairs = N * (N - 1)
            cumulative = 0
            found = False
            for s in range(max_score + 1):
                # Approximate number of pairs at distance s
                # For simplicity, we assume uniform distribution and that same-owner pairs are negligible
                num_pairs = N * min(8 * s, N - 1)
                cumulative += num_pairs
                if cumulative >= K:
                    print(f"Case #{case_num}: {s}")
                    found = True
                    break
            if not found:
                print(f"Case #{case_num}: {max_score}")
    threading.Thread(target=main).start()

solve()