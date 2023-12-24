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

def linearKeyboard():
    keyboard = insr()
    keyboard_dict = {}
    for i in range(26):
        keyboard_dict[keyboard[i]] = i
    word = insr()
    ret = 0
    for i in range(len(word)-1):
        ret += abs(keyboard_dict[word[i+1]] - keyboard_dict[word[i]])
    print(ret)
    return


if __name__ == '__main__':
    t = inp()
    for i in range(t):
        linearKeyboard()
