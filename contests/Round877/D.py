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

n, q = map(int, input().split())
string = list(input().strip())
x = [i for i in range(n) if (not (i&1) and string[i] == ")") or (i&1 and string[i]=="(")]

for __ in range(q):
    if n & 1:
        print("NO")
    else:
        index = int(input())-1
        search_index = bisect.bisect_left(x,index)
        if search_index == len(x) or x[search_index] != index:
            bisect.insort_left(x, index)
        else:
            x.pop(search_index)
        if not x or (x[0] & 1 and not x[-1] & 1):
            print("YES")
        else:
            print("NO")
