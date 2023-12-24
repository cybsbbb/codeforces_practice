
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
        matrix.append(insr())
    res = 0
    for i in range(n//2):
        for j in range(n//2):
            target = max(ord(matrix[i][j]), ord(matrix[j][n-1-i]), ord(matrix[n-1-i][n-1-j]), ord(matrix[n-1-j][i]))
            res += abs(ord(matrix[i][j]) - target)
            res += abs(ord(matrix[j][n-1-i]) - target)
            res += abs(ord(matrix[n-1-i][n-1-j]) - target)
            res += abs(ord(matrix[n-1-j][i]) - target)

    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
