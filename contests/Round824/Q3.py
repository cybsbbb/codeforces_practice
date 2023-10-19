import collections
import bisect
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


alpha = 'abcdefghijklmnopqrstuvwxyz'


def phase_shift(n, s):
    res = []
    seen = set()
    mappings = collections.defaultdict(str)
    seen_to = set()
    strs_head = {}
    strs_end = {}
    for ori in s:
        if ori in mappings:
            res.append(mappings[ori])
        else:
            for des in alpha:
                # Cannot point to itself
                if ori == des:
                    continue
                # Already been pointed
                elif des in seen_to:
                    continue
                if des not in seen and ori not in seen:
                    mappings[ori] = des
                    seen_to.add(des)
                    seen.add(ori)
                    seen.add(des)
                    strs_head[ori] = [ori, des]
                    strs_end[des] = [ori, des]
                    break
                elif des not in seen:
                    if ori in strs_end:
                        mappings[ori] = des
                        seen_to.add(des)
                        seen.add(des)
                        tmp_str = strs_end.pop(ori)
                        tmp_str.append(des)
                        strs_end[des] = tmp_str
                        strs_head[tmp_str[0]] = tmp_str
                        break
                elif des in strs_head:
                    if ori not in seen:
                        mappings[ori] = des
                        seen_to.add(des)
                        seen.add(ori)
                        tmp_str = strs_head.pop(des)
                        strs_end.pop(tmp_str[-1])
                        tmp_str.insert(0, ori)
                        strs_head[ori] = tmp_str
                        strs_end[tmp_str[-1]] = tmp_str
                        break
                    elif ori in strs_end:
                        if strs_end[ori][0] == des:
                            if len(strs_end[ori]) == 26:
                                mappings[ori] = des
                                seen_to.add(des)
                                break
                            else:
                                continue
                        mappings[ori] = des
                        seen_to.add(des)
                        c_end = strs_end.pop(ori)
                        strs_head.pop(c_end[0])
                        a_head = strs_head.pop(des)
                        strs_end.pop(a_head[-1])
                        tmp_str = c_end + a_head
                        strs_head[tmp_str[0]] = tmp_str
                        strs_end[tmp_str[-1]] = tmp_str
                        break

            res.append(mappings[ori])

    print(''.join(res))


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        n = inp()
        s = insr()
        phase_shift(n, s)

