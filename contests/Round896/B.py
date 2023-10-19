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
    n, k, a, b = inlt()
    cities = []
    for i in range(n):
        cities.append(inlt())
    res = abs(cities[a-1][0] - cities[b-1][0]) + abs(cities[a-1][1] - cities[b-1][1])
    min_dis_a = 10 ** 10
    min_dis_b = 10 ** 10
    for i in range(1, k+1):
        min_dis_a = min(min_dis_a, abs(cities[a - 1][0] - cities[i - 1][0]) + abs(cities[a - 1][1] - cities[i - 1][1]))
        min_dis_b = min(min_dis_b, abs(cities[b - 1][0] - cities[i - 1][0]) + abs(cities[b - 1][1] - cities[i - 1][1]))
    res = min(res, min_dis_a + min_dis_b)
    print(res)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
