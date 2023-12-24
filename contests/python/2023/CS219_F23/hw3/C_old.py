import collections
import math
import sys

input = sys.stdin.readline

def inlt():
    return (list(map(int, input().split())))

n, r = inlt()
points_dict = collections.defaultdict(int)
for _ in range(n):
    x, y, indicate = inlt()
    if indicate == 1:
        points_dict[(x, y)] += 3
    else:
        points_dict[(x, y)] += 1
points = list(points_dict.keys())
m = len(points)

dis_matrix = [[0] * m for _ in range(m)]
for i in range(m):
    for j in range(i+1, m):
        dis_matrix[i][j] = math.sqrt((points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) +
                                     (points[i][1] - points[j][1]) * (points[i][1] - points[j][1]))
        dis_matrix[j][i] = dis_matrix[i][j]

cta_delta_dict = dict()

ans = 0
for i in range(m):
    intervals = []
    center_point = points_dict[points[i]]
    beginning = 0
    possible = center_point
    for j in range(m):
        if i == j:
            continue
        cur_point = points_dict[points[j]]
        dist = dis_matrix[i][j]

        if dist <= 2 * r:
            possible += cur_point
            if (i, j) not in cta_delta_dict:
                cta = math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])
                delta = math.acos(dist / 2.0 / r)
                if cta < 0:
                    cta += 2 * math.pi
                cta_delta_dict[(j, i)] = (cta - math.pi, delta)
            else:
                cta, delta = cta_delta_dict[(i, j)]
                if cta < 0:
                    cta += 2 * math.pi
            a1, a2 = (cta - delta) % (2 * math.pi), (cta + delta) % (2 * math.pi)
            intervals.append((a1, -cur_point))
            intervals.append((a2, cur_point))
            if a1 > a2:
                beginning += cur_point
    if possible <= ans:
        continue
    intervals.sort()
    res = center_point + beginning
    for k in range(len(intervals)):
        res -= intervals[k][1]
        ans = max(ans, res)

print(ans)
exit()
