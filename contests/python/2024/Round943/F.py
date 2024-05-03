import bisect
import collections
import sys
import heapq
import math

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
    n, q = inlt()
    a = inlt()

    prefix_xor_dict = collections.defaultdict(list)
    prefix_xor_dict[0].append(0)
    prefix_xor = [0]
    for i in range(n):
        prefix_xor.append(prefix_xor[-1] ^ a[i])
        prefix_xor_dict[prefix_xor[-1]].append(i + 1)

    suffix_xor_dict = collections.defaultdict(collections.deque)
    suffix_xor_dict[0].append(n + 1)
    suffix_xor = collections.deque([0])
    for i in range(n)[::-1]:
        suffix_xor.appendleft(suffix_xor[0] ^ a[i])
        suffix_xor_dict[suffix_xor[0]].appendleft(i)

    for _ in range(q):
        l, r = inlt()
        if prefix_xor[r] ^ prefix_xor[l - 1] == 0:
            print("YES")
            continue
        else:
            left_xor = prefix_xor[l - 1]
            right_idx = bisect.bisect_left(prefix_xor_dict[left_xor], r)
            if right_idx - 1 >= 0 and prefix_xor_dict[left_xor][right_idx - 1] >= l:
                right_pos = prefix_xor_dict[left_xor][right_idx - 1]
            else:
                print("NO")
                continue

            right_xor = suffix_xor[r]
            left_idx = bisect.bisect_left(suffix_xor_dict[right_xor], l - 1)
            if left_idx < len(suffix_xor_dict[right_xor]) and suffix_xor_dict[right_xor][left_idx] < r:
                left_pos = suffix_xor_dict[right_xor][left_idx]
            else:
                print("NO")
                continue

            if right_pos > left_pos:
                print("YES")
            else:
                print("NO")

    print()
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
