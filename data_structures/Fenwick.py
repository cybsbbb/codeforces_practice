
n = 1 << 20
fenwick = [0] * (n +1)
def lowbit(x):
    return x & -x

def update(index, d):
    while index <= n:
        fenwick[index] += d
        index += lowbit(index)

def getsum(index):
    res = 0
    while index > 0:
        res += fenwick[index]
        index -= lowbit(index)
    return res


