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


def foodforAnimals():

    a, b, c, x, y = inlt()

    x -= a
    x = max(0, x)
    y -= b
    y = max(0, y)

    if (x + y) <= c:
        print(f"YES")
    else:
        print(f"NO")
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        foodforAnimals()
