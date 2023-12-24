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
    N = inp()
    time = inlt()
    init_time = inlt()
    res_time = distribution(N, time, init_time)
    for time in res_time:
        print(time)





