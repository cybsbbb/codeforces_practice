from collections import deque
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


def dot(x, y):
    return x[0] * y[0] + x[1] * y[1]

def cross(x, y):
    return x[0] * y[1] - x[1] * y[0]


def check_intersect(A, B, C, D):
    ab = (B[0] - A[0], B[1] - A[1])
    ac = (C[0] - A[0], C[1] - A[1])
    ad = (D[0] - A[0], D[1] - A[1])
    ca = (A[0] - C[0], A[1] - C[1])
    cb = (B[0] - C[0], B[1] - C[1])
    cd = (D[0] - C[0], D[1] - C[1])
    if cross(ab, ad) * cross(ab, ac) <= 0 and cross(cd, ca) * cross(cd, cb) <= 0:
        return True, abs(cross(ab, cd) / 2)
    else:
        return False, 0


def check_inside(A, B, C, D):
    ba = (A[0] - B[0], A[1] - B[1])
    bc = (C[0] - B[0], C[1] - B[1])
    bd = (D[0] - B[0], D[1] - B[1])
    ca = (A[0] - C[0], A[1] - C[1])
    cb = (B[0] - C[0], B[1] - C[1])
    cd = (D[0] - C[0], D[1] - C[1])
    da = (A[0] - D[0], A[1] - D[1])
    db = (B[0] - D[0], B[1] - D[1])
    dc = (C[0] - D[0], C[1] - D[1])
    ab = (B[0] - A[0], B[1] - A[1])
    ac = (C[0] - A[0], C[1] - A[1])
    ad = (D[0] - A[0], D[1] - A[1])
    if cross(ba, bc) * cross(ba, bd) <= 0 and cross(ca, cb) * cross(ca, cd) <= 0 and cross(da, db) * cross(da, dc) <= 0:
        return True, abs(cross(ab, ac) / 2) + abs(cross(ab, ad) / 2) + abs(cross(ac, ad) / 2)
    else:
        return False, 0

A = inlt()
B = inlt()
C = inlt()
D = inlt()

indicate, res = check_intersect(A, B, C, D)
if indicate is True:
    print(res)
    exit()
indicate, res = check_intersect(A, C, B, D)
if indicate is True:
    print(res)
    exit()
indicate, res = check_intersect(A, D, B, C)
if indicate is True:
    print(res)
    exit()
indicate, res = check_inside(A, D, B, C)
if indicate is True:
    print(res)
    exit()
indicate, res = check_inside(B, A, C, D)
if indicate is True:
    print(res)
    exit()
indicate, res = check_inside(C, A, B, D)
if indicate is True:
    print(res)
    exit()
indicate, res = check_inside(D, A, B, C)
if indicate is True:
    print(res)
    exit()

print(0.0)
exit()
