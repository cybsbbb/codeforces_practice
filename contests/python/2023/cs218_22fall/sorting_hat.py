import collections
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
    t = inp()
    house_dict = collections.defaultdict(list)
    for i in range(t):
        name, house = input().split()
        house_dict[house].append(name)

    for key in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
        print(key)
        for name in sorted(house_dict[key]):
            print(name)
