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
    Sheldon = input()[:-1]
    Leonard = input()[:-1]
    if Sheldon == 'Paper':
        if Leonard == 'Rock' or Leonard == 'Spock':
            print(f"Sheldon wins the game!")
            return
        elif Leonard == 'Scissors' or Leonard == 'Lizard':
            print(f"Leonard wins the game!")
            return
        else:
            print('Tie!')
            return
    elif Sheldon == 'Rock':
        if Leonard == 'Lizard' or Leonard == 'Scissors':
            print(f"Sheldon wins the game!")
            return
        elif Leonard == 'Paper' or Leonard == 'Spock':
            print(f"Leonard wins the game!")
            return
        else:
            print('Tie!')
            return
    elif Sheldon == 'Scissors':
        if Leonard == 'Paper' or Leonard == 'Lizard':
            print(f"Sheldon wins the game!")
            return
        elif Leonard == 'Spock' or Leonard == 'Rock':
            print(f"Leonard wins the game!")
            return
        else:
            print('Tie!')
            return
    elif Sheldon == 'Lizard':
        if Leonard == 'Spock' or Leonard == 'Paper':
            print(f"Sheldon wins the game!")
            return
        elif Leonard == 'Rock' or Leonard == 'Scissors':
            print(f"Leonard wins the game!")
            return
        else:
            print('Tie!')
            return
    elif Sheldon == 'Spock':
        if Leonard == 'Scissors' or Leonard == 'Rock':
            print(f"Sheldon wins the game!")
            return
        elif Leonard == 'Lizard' or Leonard == 'Paper':
            print(f"Leonard wins the game!")
            return
        else:
            print('Tie!')
            return





if __name__ == '__main__':
    t = 1
    for i in range(t):
        solution()
