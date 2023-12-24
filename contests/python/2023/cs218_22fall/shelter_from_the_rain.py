import collections
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


if __name__ == '__main__':
    n, m, b = inlt()
    students = []
    for i in range(n):
        x, y, r = inlt()
        students.append((x, y, r))
    shelters = []
    for i in range(m):
        x, y = inlt()
        shelters.append((x, y))

    students_map = collections.defaultdict(list)

    for s_idx in range(n):
        sx, sy, sr = students[s_idx]
        for t_idx in range(m):
            tx, ty = shelters[t_idx]
            # print(((sx - tx) ** 2 + (sy - ty) ** 2), (b * sr) ** 2)
            if ((sx - tx) ** 2 + (sy - ty) ** 2) <= (b * sr) ** 2:
                students_map[s_idx].append(t_idx)

    map_shelter = dict()
    visited_shelter = set()

    def match(student):
        for shelter in students_map[student]:
            if shelter not in visited_shelter:
                visited_shelter.add(shelter)
                if shelter not in map_shelter or match(map_shelter[shelter]) is True:
                    map_shelter[shelter] = student
                    return True
        return False

    res = 0
    for i in range(n):
        visited_shelter = set()
        if match(i) is True:
            res += 1

    print(n - res)
