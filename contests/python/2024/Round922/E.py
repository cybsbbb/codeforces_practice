import random
import sys

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


t = inp()
for i in range(t):
    n = inp()
    ans = [0] * n

    def quick_sort(arr, l, r):
        if not arr:
            return
        rd = random.randint(0, len(arr) - 1)
        ch = '#'
        while ch != '=':
            print("?", arr[rd], flush=True)
            ch = input().strip()
        left = []
        right = []
        for i in range(len(arr)):
            if i == rd:
                continue
            print("?", arr[i], flush=True)
            ch = input().strip()
            if ch == '<':
                left.append(arr[i])
            else:
                right.append(arr[i])
            print("?", arr[rd], flush=True)
            input().strip()
        ans[arr[rd] - 1] = l + len(left)
        quick_sort(left, l, l + len(left) - 1)
        quick_sort(right, l + len(left) + 1, r)

    arr = list(range(1, n + 1))
    quick_sort(arr, 1, n)
    print("!", *ans, flush=True)
