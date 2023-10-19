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
    N = inp()
    points = []
    for i in range(N):
        x, y = inlt()
        points.append([y, x])
    directions = insr()
    for i in range(N):
        points[i].append(directions[i])
    points.sort()

    y_flag = False
    cur_y = points[0][0]
    if_right = (points[0][2] == 'R')


    for point in points[1:]:
        if point[0] == cur_y:
            if point[2] == 'R':
                if_right = True
            elif point[2] == 'L' and if_right == True:
                print("Yes")
                y_flag = True
                break
        else:
            cur_y = point[0]
            if_right = (point[2] == 'R')

    if y_flag == False:
        print("No")
