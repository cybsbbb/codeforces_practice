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


if __name__ == '__main__':
    m = inp()
    constellation = []
    for i in range(m):
        x, y = inlt()
        constellation.append((x, y))
    constellation.sort()
    n = inp()
    picture = []
    for i in range(n):
        x, y = inlt()
        picture.append((x, y))
    picture.sort()
    picture_set = set(picture)

    for start_x, start_y in picture:
        shift_x, shift_y = start_x - constellation[0][0], start_y - constellation[0][1]
        flag = True
        for constellation_x, constellation_y in constellation[1:]:
            if (constellation_x + shift_x, constellation_y + shift_y) not in picture_set:
                flag = False
                break
        if flag == True:
            print(shift_x, shift_y)
            break
