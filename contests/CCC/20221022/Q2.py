import sys
input = sys.stdin.readline


def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input().strip()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


if __name__ == '__main__':
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107]
    a, b, c, d = inlt()

    res = 0
    upper = 107

    memory = [[0]*upper for i in range(upper)]


    for i in range(1, upper):
        for j in range(1, upper):
            tmp = 0
            for n1 in range(1, i+1):
                for n2 in range(1, j+1):
                    if gcd(n1, n2) == 1:
                        tmp += 1
            memory[i][j] = tmp

    print(memory)
    for i in range(13):
        print(memory[i])

    print(memory[b][d] - memory[a-1][d] - memory[b][c-1] + memory[a-1][c-1])





    # for i in range(a, b+1):
    #     for j in range(c, d+1):
    #         if i == 1 or j == 1:
    #             res += 1
    #             continue
    #         if gcd(i, j) == 1:
    #             res += 1
    # print(res)
