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
    n = inp()
    matrix = []
    for i in range(n):
        matrix.append(inlt())

    ans = [0] * n
    for k in range(30):
        for i in range(n):
            flag = True
            for j in range(n):
                if i == j:
                    continue
                if not (matrix[i][j] >> k) & 1:
                    flag = False
            if flag == True:
                ans[i] += (1 << k)

    for i in range(n):
        for j in range(n):
            if i != j and (ans[i] | ans[j]) != matrix[i][j]:
                print("NO")
                return
    print("YES")
    print(*ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
