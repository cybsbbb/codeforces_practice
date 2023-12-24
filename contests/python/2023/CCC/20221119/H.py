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


if __name__ == '__main__':
    N = list(map(int, list(input()[:-1])))
    pre_sum = [N[0]]
    for n in N[1:]:
        pre_sum.append(pre_sum[-1] + n)
    res = []
    tmp = 0
    for n in pre_sum[::-1]:
        n += tmp
        res.append(str(n % 10))
        tmp = n // 10
    if tmp != 0:
        print(str(tmp) + ''.join(res[::-1]))
    else:
        print(''.join(res[::-1]))
