import collections
import math
import sys
input = sys.stdin.readline


def find_sqrt(X):
    if X < 2:
        return X
    res = 0
    start = 1
    end = X // 2
    while start <= end:
        mid = (start + end) // 2
        sqr = mid * mid

        if sqr == X:
            return mid
        elif sqr < X:
            start = mid + 1
            res = mid
        else:
            end = mid - 1
    return res


def q7(sqrt_X):
    sqrt_sqrt_X = find_sqrt(sqrt_X)
    A_sqrt_X = [0]*max(sqrt_sqrt_X+1, 10)
    A_sqrt_X[1] = 1
    pre_sum = [0]*max(sqrt_sqrt_X+1, 10)
    pre_sum[1] = 3*1
    for sqrt_itr in range(2, sqrt_sqrt_X+1):
        sqrt_sqrt_itr = find_sqrt(sqrt_itr)
        A_sqrt_X[sqrt_itr] = A_sqrt_X[sqrt_sqrt_itr] * (sqrt_itr - sqrt_sqrt_itr*sqrt_sqrt_itr+1) + pre_sum[sqrt_sqrt_itr-1]
        pre_sum[sqrt_itr] = A_sqrt_X[sqrt_itr] * (2*sqrt_itr+1) + pre_sum[sqrt_itr-1]
    sqrt_sqrt_X = find_sqrt(sqrt_X)
    res = A_sqrt_X[sqrt_sqrt_X] * (sqrt_X - sqrt_sqrt_X * sqrt_sqrt_X + 1) + pre_sum[sqrt_sqrt_X - 1]

    return res


if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        X = int(input())
        sqrt_X = find_sqrt(X)
        print(q7(sqrt_X))
