import math
import sys

input = sys.stdin.readline

def inlt():
    return (list(map(int, input().split())))

n, r = inlt()
points = []
for _ in range(n):
    x, y, indicate = inlt()
    point = 3 if indicate == 1 else 1
    points.append((x, y, point))


intervals = [[] for _ in range(n)]
possiables = [points[i][2] for i in range(n)]

for i in range(n):
    for j in range(i+1, n):
        dist = math.sqrt((points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) +
                         (points[i][1] - points[j][1]) * (points[i][1] - points[j][1]))
        if dist <= 2 * r:
            possiables[i] += points[j][2]
            possiables[j] += points[i][2]
            delta = math.acos(dist / 2.0 / r)
            # i to j
            cta = math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])
            cta = cta + 2 * math.pi if cta < 0 else cta
            a1, a2 = cta - delta, cta + delta
            if a1 < 0:
                intervals[i].append((a1 + 2 * math.pi, -points[j][2]))
                intervals[i].append((a2 + 2 * math.pi, points[j][2]))
            else:
                intervals[i].append((a1, -points[j][2]))
                intervals[i].append((a2, points[j][2]))
                intervals[i].append((a1 + 2 * math.pi, -points[j][2]))
                intervals[i].append((a2 + 2 * math.pi, points[j][2]))
            # j to i
            cta -= math.pi
            cta = cta + 2 * math.pi if cta < 0 else cta
            a1, a2 = cta - delta, cta + delta
            if a1 < 0:
                intervals[j].append((a1 + 2 * math.pi, -points[i][2]))
                intervals[j].append((a2 + 2 * math.pi, points[i][2]))
            else:
                intervals[j].append((a1, -points[i][2]))
                intervals[j].append((a2, points[i][2]))
                intervals[j].append((a1 + 2 * math.pi, -points[i][2]))
                intervals[j].append((a2 + 2 * math.pi, points[i][2]))

ans = 0

for i in range(n):
    if possiables[i] <= ans:
        continue
    interval = intervals[i]
    interval.sort()
    res = points[i][2]
    for _, num in interval:
        res -= num
        if res > ans:
            ans = res
print(ans)

