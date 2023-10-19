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


def distribution(N, time, init_time):
    start = init_time.index(min(init_time))
    pre = start
    cur = (start + 1) % N

    while cur != start:
        init_time[cur] = min(init_time[cur], init_time[pre] + time[pre])
        pre = cur
        cur = (pre + 1) % N

    return init_time


if __name__ == '__main__':
    S = insr()
    N = len(S)

    dp_pre_pre = [0 for j in range(N) for i in range(26)]
    dp_pre = [0 for j in range(N) for i in range(26)]
    for i in range(N):
        c = S[i]
        c_int = ord(c) - ord('a')







