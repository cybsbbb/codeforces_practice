import collections
import sys
import heapq

input = sys.stdin.readline

def inp():
    return (int(input()))
def inlt():
    return (list(map(int, input().split())))
def insr():
    s = input()
    return (list(s[:len(s) - 1]))
def invr():
    return (map(int, input().split()))


def solution():
    k = inp()
    galaxies = inlt()
    n = 2 << k
    pre_xor = [0]
    for num in galaxies:
        pre_xor.append(pre_xor[-1] ^ num)

    mem_high_bits = [-1] * (1 << k)
    mem_high_bits[0] = 0
    mem_low_bits = [(-1, -1) for _ in range(1 << k)]

    for i in range(1, n+1):
        if mem_high_bits[pre_xor[i] >> k] != -1:
            whole_xor = pre_xor[mem_high_bits[pre_xor[i] >> k]] ^ pre_xor[i]
            start, end = mem_low_bits[whole_xor]
            if start == -1:
                mem_low_bits[whole_xor] = (mem_high_bits[pre_xor[i] >> k], i)
            else:
                if end < mem_high_bits[pre_xor[i] >> k] + 1:
                    print(f"{start + 1} {end} {mem_high_bits[pre_xor[i] >> k] + 1} {i}")
                else:
                    print(f"{min(start + 1, mem_high_bits[pre_xor[i] >> k] + 1)} {max(start + 1, mem_high_bits[pre_xor[i] >> k] + 1)-1} {end+1} {i}")
                return
        mem_high_bits[pre_xor[i] >> k] = i


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
