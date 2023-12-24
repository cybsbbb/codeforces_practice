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



def helper(left, right):
    res = []
    if right == left:
        return res
    for i in range(left, right-1, 2):
        res.append(i)
    for i in range(right - 4, left - 1, -2):
        res.append(i)
    return res



def solution():
    n = inp()
    a = inlt()
    val = 0
    for num in a:
        val ^= num
    if val == 1:
        print("NO")
        return
    if n % 2 == 1:
        res = helper(1, n)
        print("YES")
        print(len(res))
        print(*res)
        return
    elif n % 2 == 0:
        val = a[0]
        if val == 0:
            res = helper(2, n)
            print("YES")
            print(len(res))
            print(*res)
            return
        cur_idx = 0
        while cur_idx + 2 < n:
            val = val ^ a[cur_idx + 1] ^ a[cur_idx + 2]
            cur_idx += 2
            if val == 0:
                res_left = helper(1, cur_idx + 1)
                res_right = helper(cur_idx + 2, n)
                res = res_left + res_right
                print("YES")
                print(len(res))
                print(*res)
                return

        print("NO")
        return





if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
