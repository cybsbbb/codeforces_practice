import collections
import sys

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


def icpc(s):
    if s == '':
        return -1
    count = collections.Counter(s)
    max_expression = max(count['L'] + count['R'], count['('], count[')'], count[','])
    if max_expression == 0:
        for idx in range(len(s)):
            if s[idx] == '?':
                s[idx] = '9'
        return int(''.join(s))
    if max_expression != 0 and len(s) < max_expression * 5 + 1:
        return -1
    else:
        if s[-1] != ')' and s[-1] != '?':
            return -1
        if s[1] != '(' and s[1] != '?':
            return -1
        if s[0] != 'R' and s[0] != 'L' and s[0] != '?':
            return -1
        res = -1
        for i in range(3, len(s)-2):
            if s[i] != ',' and s[i] != '?':
                continue
            left = icpc(s[2:i])
            right = icpc(s[i+1:-1])
            if left >= 0 and right >= 0:
                if s[0] == '?':
                    res = max(res, max(left, right))
                if s[0] == 'R':
                    res = max(res, right)
                if s[0] == 'L':
                    res = max(res, left)
        return res


if __name__ == '__main__':
    s = insr()
    res = icpc(s)
    if res >= 0:
        print(res)
    else:
        print('invalid')
