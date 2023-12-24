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


ordinary_list = []
for i in range(1, 11):
    for j in range(1, 10):
        ordinary_list.append(int(str(j) * i))


def ordinary(n):
    for i in range(len(ordinary_list)):
        if ordinary_list[i] > n:
            print(i)
            return
    print(len(ordinary_list))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        n = inp()
        ordinary(n)
