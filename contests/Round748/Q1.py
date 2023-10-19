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

def elections(numbers):
    largest = max(numbers)
    num_largest = numbers.count(largest)
    ret = []
    for i in range(3):
        if numbers[i] == largest and num_largest > 1:
            ret.append("1")
        elif numbers[i] == largest and num_largest == 1:
            ret.append("0")
        else:
            ret.append(str(largest + 1 - numbers[i]))
    print(' '.join(ret))
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        numbers = inlt()
        elections(numbers)
