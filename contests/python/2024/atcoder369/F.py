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


h, w, n = inlt()
stones = []
for i in range(n):
    ri, ci = inlt()
    stones.append((ri, ci))
stones.sort(key=lambda x: (x[0], -x[1]))
st = []
pre_mapping = dict()
for ri, ci in stones:
    stone = 1
    while st and st[-1][1] <= ci:
        pre_r, pre_c, stone_pre = st.pop()
        stone += stone_pre
        pre_mapping[(ri, ci)] = pre_r, pre_c
    st.append((ri, ci, stone))


max_tot = 0
max_ri, max_ci = h - 1, w - w
for ri, ci, stone in st:
    if stone > max_tot:
        max_tot = stone
        max_ri, max_ci = ri, ci

ans = []
ans += ['R'] * (w - max_ci) + ['D'] * (h - max_ri)
while (max_ri, max_ci) in pre_mapping:
    nxt_ri, nxt_ci = pre_mapping[(max_ri, max_ci)]
    ans += ['R'] * (max_ci - nxt_ci) + ['D'] * (max_ri - nxt_ri)
    max_ri, max_ci = nxt_ri, nxt_ci
ans += ['R'] * (max_ci - 1) + ['D'] * (max_ri - 1)

print(max_tot)
print(''.join(ans[::-1]))





