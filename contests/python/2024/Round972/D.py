import sys
import threading


def main():
    import math
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))

        GCD_total = a[0]
        for num in a + b:
            GCD_total = math.gcd(GCD_total, num)

        impossible = False
        necessary_positions = []
        harmful_positions = []

        for i in range(n):
            a_mod = a[i] % GCD_total
            b_mod = b[i] % GCD_total
            if a_mod != 0 and b_mod != 0:
                impossible = True
                break
            elif a_mod != 0 and b_mod == 0:
                necessary_positions.append(i)
            elif a_mod == 0 and b_mod != 0:
                harmful_positions.append(i)
            # else both divisible, do nothing

        if impossible:
            print(f"{math.gcd(*a) + math.gcd(*b)} 0")
            continue

        if not necessary_positions:
            # No need to swap, maximum sum achieved without swapping
            max_sum = 2 * GCD_total
            ways = n * (n + 1) // 2
            print(f"{max_sum} {ways}")
            continue

        min_necessary = min(necessary_positions)
        max_necessary = max(necessary_positions)

        # Check if there are harmful positions within [min_necessary, max_necessary]
        harmful_within = [pos for pos in harmful_positions if min_necessary <= pos <= max_necessary]
        if harmful_within:
            # Cannot avoid swapping harmful positions
            print(f"{math.gcd(*a) + math.gcd(*b)} 0")
            continue

        # Number of ways to choose l and r
        ways = (min_necessary + 1) * (n - max_necessary)
        max_sum = 2 * GCD_total
        print(f"{max_sum} {ways}")


threading.Thread(target=main).start()
