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
    a = inlt()

    while not all((a[(i + 1) % n] == 0 or a[(i) % n] == 0 or a[(i - 1) % n] == 0) for i in range(n)):
        for i in range(n):
            a[(i + 1) % n] = max(0, a[(i + 1) % n] - a[i])
    ans = []
    pre0 = True if a[-1] == 0 else False
    for i in range(n):
        if a[i] == 0:
            pre0 = True
        elif a[i] != 0:
            if pre0 is True:
                ans.append(i + 1)
            pre0 = False

    print(len(ans))
    print(*ans)
