import sys

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


n = inp()
funness_list = inlt()
m = max(funness_list)
fenwick = [0] * (m + 5)
def lowbit(x):
    return x & -x
def update(index, d):
    while index <= (m + 4):
        fenwick[index] = max(fenwick[index], d)
        index += lowbit(index)
def getsum(index):
    res = 0
    while index > 0:
        res = max(res, fenwick[index])
        index -= lowbit(index)
    return res

for i in range(n):
    funness = funness_list[i]
    tot_funness = funness * (n - i)
    pre_max = getsum(funness - 1)
    cur_val = pre_max + tot_funness
    update(funness, cur_val)

print(getsum(m + 1))
exit()

