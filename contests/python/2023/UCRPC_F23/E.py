import collections
import sys
import heapq

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


def solution():
    ciphertext = insr()
    plaintext = insr()
    target = insr()
    decrypt = dict()
    encrypt = dict()
    n = len(ciphertext)
    for i in range(n):
        cipher_chr = ciphertext[i]
        plain_chr = plaintext[i]
        if cipher_chr not in decrypt and plain_chr not in encrypt:
            decrypt[cipher_chr] = plain_chr
            encrypt[plain_chr] = cipher_chr
        if cipher_chr in decrypt and decrypt[cipher_chr] != plain_chr:
            print('Failed')
            return
        if plain_chr in encrypt and encrypt[plain_chr] != cipher_chr:
            print('Failed')
            return
    if len(decrypt) != 26:
        print('Failed')
        return

    res = []
    for i in range(len(target)):
        res.append(decrypt[target[i]])
    print(''.join(res))
    return


if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
