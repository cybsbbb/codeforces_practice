import collections
import sys
import math
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


def PerfectlyFine():
    n = inp()
    book_dict = dict()
    for i in range(n):
        time, label = input().split()
        time = int(time)
        if label not in book_dict:
            book_dict[label] = time
        else:
            book_dict[label] = min(book_dict[label], time)
    res = 1000000
    if '01' in book_dict and '10' in book_dict:
        res = min(res, book_dict['01'] + book_dict['10'])
    if '11' in book_dict:
        res = min(res, book_dict['11'])

    if res == 1000000:
        print(-1)
        return -1
    else:
        print(res)
        return res


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        PerfectlyFine()
