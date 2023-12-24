import sys
input = sys.stdin.readline


def inp():
    return(int(input().strip()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


def find_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


if __name__ == '__main__':
    x = inp()
    primes = find_primes(x)
    primes_set = set(primes)
    res = 0
    while x >= 4:
        i = 0
        while primes[i] <= x // 2:
            diff = x - primes[i]
            if diff in primes_set:
                res += 1
                x = diff - primes[i]
                break
            i += 1
    print(res)
