import heapq
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


def busy(n, k, tasks):
    if k == 1:
        print("{:.8f}".format(sum(tasks)))
        return 0
    if len(tasks) < k:
        print("{:.8f}".format(0.0))
        return 0
    tasks.sort(reverse=True)
    top_k = tasks[:k][::-1]
    res = top_k[0]

    remaining = sum(tasks[k:])
    machine_num = 1
    for idx in range(1, len(top_k)):
        if machine_num * (top_k[idx] - top_k[idx - 1]) <= remaining:
            remaining -= machine_num * (top_k[idx] - top_k[idx - 1])
            machine_num += 1
            res = top_k[idx]
        else:
            res += remaining / machine_num
            remaining = 0
            break
    if remaining > 0:
        res += remaining / k
    print("{:.8f}".format(res))
    return 0


if __name__ == '__main__':
    while True:
        n, k = inlt()
        if n == -1 and k == -1:
            break
        tasks = inlt()
        busy(n, k, tasks)


