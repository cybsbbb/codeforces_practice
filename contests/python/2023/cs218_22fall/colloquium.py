from collections import defaultdict
import sys
input = sys.stdin.readline

def colloquium(n, s):

    cur_state = defaultdict(lambda: defaultdict(int))
    nxt_state = defaultdict(lambda: defaultdict(int))
    cur_state[""][""] = 0

    score_dict = {'TTT': 20, 'TTS': 40, 'TTA': 40, 'TST': 40, 'TSS': 40, 'TSA': 60, 'TAT': 40,
                      'TAS': 60, 'TAA': 40, 'STT': 40, 'STS': 40, 'STA': 60, 'SST': 40, 'SSS': 20,
                      'SSA': 40, 'SAT': 60, 'SAS': 40, 'SAA': 40, 'ATT': 40, 'ATS': 60, 'ATA': 40,
                      'AST': 60, 'ASS': 40, 'ASA': 40, 'AAT': 40, 'AAS': 40, 'AAA': 20, 'TT': 20,
                      'TS': 40, 'TA': 40, 'ST': 40, 'SS': 20, 'SA': 40, 'AT': 40, 'AS': 40, 'AA': 20,
                      'T': 20, 'S': 20, 'A': 20}

    for i in range(n):
        # nxt_state.clear()
        nxt_state = defaultdict(lambda: defaultdict(int))
        for state1 in cur_state:
            for state2 in cur_state[state1]:
                cur_val = cur_state[state1][state2]
                tail1 = state1 + s[i]
                tail2 = state2 + s[i]
                nxt_state[tail1[-2:]][state2] = max(nxt_state[tail1[-2:]][state2], cur_val + score_dict[tail1])
                nxt_state[state1][tail2[-2:]] = max(nxt_state[state1][tail2[-2:]], cur_val + score_dict[tail2])

        cur_state, nxt_state = nxt_state, cur_state

    res = 0
    for state1 in cur_state:
        for state2 in cur_state[state1]:
            res = max(res, cur_state[state1][state2])

    print(res)


n = int(input())
s = input()
colloquium(n, s)
