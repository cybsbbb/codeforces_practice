import collections
import sys
import bisect
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
    n, q = inlt()
    cur_len = 0

    length_before_type2 = []
    before_type2_info = []
    stack = []
    for _ in range(n):
        b, x = inlt()
        if cur_len > 10 ** 18:
            continue
        if b == 1:
            cur_len += 1
            stack.append(x)
        if b == 2:
            length_before_type2.append(cur_len)
            cur_remain = 0
            tmp_dict = collections.defaultdict()
            while stack:
                x_end = stack.pop()
                tmp_dict[cur_remain] = x_end
                cur_remain -= 1
            before_type2_info.append(tmp_dict)
            cur_len *= (x + 1)
    length_before_type2.append(cur_len)
    cur_remain = 0
    tmp_dict = collections.defaultdict()
    while stack:
        x_end = stack.pop()
        tmp_dict[cur_remain] = x_end
        cur_remain -= 1
    before_type2_info.append(tmp_dict)

    q = inlt()
    ans = []
    for qi in q:
        for seg_len_idx in range(len(length_before_type2))[::-1]:
            seg_len = length_before_type2[seg_len_idx]
            seg_dict = before_type2_info[seg_len_idx]

            seg_loc = (qi - 1) % seg_len + 1 - seg_len
            if seg_loc in seg_dict:
                ans.append(seg_dict[seg_loc])
                break
            else:
                qi = seg_loc + seg_len

    print(*ans)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        solution()
