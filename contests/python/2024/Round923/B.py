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
    a = inlt()
    cur_letter = 0
    stat = [0] * 26
    ans = []
    for i in range(n):
        if a[i] == 0:
            ans.append(chr(ord('a') + cur_letter))
            stat[cur_letter] += 1
            cur_letter += 1
        else:
            for j in range(cur_letter):
                if stat[j] == a[i]:
                    ans.append(chr(ord('a') + j))
                    stat[j] += 1
                    break
    print(''.join(ans))
    return



if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
