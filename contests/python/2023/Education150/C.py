import collections
import sys
import math
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

values = {'A': 1, 'B': 10, 'C': 100, 'D': 1000, 'E': 10000}
value2char = {1: 'A', 10: 'B', 100: 'C', 1000: 'D', 10000: 'E'}
values_pre = {10000: 1000, 1000: 100, 100: 10, 10: 1}


def solution():
    s = insr()
    max_value = values[s[-1]]
    ranom = [max_value]

    for c in s[:-1][::-1]:
        value = values[c]
        if value < max_value:
            ranom.append(-value)
        else:
            ranom.append(value)
            max_value = value
    ranom = ranom[::-1]
    original_val = sum(ranom)

    res = 0
    tmp = 0
    for num in ranom:
        if num == 10000:
            continue
        res = max(res, 10000 - num - tmp)
        if num > 0:
            tmp += num * 2

    counter = collections.Counter(s)
    for value in [10000, 1000, 100, 10]:
        pre_value = values_pre[value]
        flag = False
        tmp = 0
        if counter[value2char[value]] > 0:
            for num in ranom[::-1]:
                if abs(num) > value:
                    break
                if num == value:
                    if flag == False:
                        flag = True
                    else:
                        break
                if flag == True and -num == pre_value:
                    tmp += 2 * pre_value
            res = max(res, tmp - value + pre_value)
        else:
            continue

    print(original_val + res)


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
