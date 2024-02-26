import collections
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


def solution():
    n, k = inlt()
    a = inlt()
    x = inlt()
    monster = list(zip(x, a))
    monster.sort(key=lambda x: abs(x[0]))
    # print(monster)

    cur_acc = 0
    for xi, ai, in monster:
        cur_acc += ai
        if k * abs(xi) < cur_acc:
            print("NO")
            return

    print("YES")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
