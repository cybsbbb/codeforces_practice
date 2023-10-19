import sys
input = sys.stdin.readline


def colloquium(n, s):
    dp_pre = [[0 for k in range(13)] for j in range(13)]
    dp_cur = [[0 for k in range(13)] for j in range(13)]

    idx_list = ["", "T", "S", "A", "TT", "TS", "TA", "ST", "SS", "SA", "AT", "AS", "AA"]

    attention_dict = {'TTT': 20, 'TTS': 40, 'TTA': 40, 'TST': 40, 'TSS': 40, 'TSA': 60, 'TAT': 40,
                'TAS': 60, 'TAA': 40, 'STT': 40, 'STS': 40, 'STA': 60, 'SST': 40, 'SSS': 20,
                'SSA': 40, 'SAT': 60, 'SAS': 40, 'SAA': 40, 'ATT': 40, 'ATS': 60, 'ATA': 40,
                'AST': 60, 'ASS': 40, 'ASA': 40, 'AAT': 40, 'AAS': 40, 'AAA': 20, 'TT': 20,
                'TS': 40, 'TA': 40, 'ST': 40, 'SS': 20, 'SA': 40, 'AT': 40, 'AS': 40, 'AA': 20,
                'T': 20, 'S': 20, 'A': 20}

    state_dict = {'TTT': 4, 'TTS': 5, 'TTA': 6, 'TST': 7, 'TSS': 8, 'TSA': 9, 'TAT': 10,
                  'TAS': 11, 'TAA': 12, 'STT': 4, 'STS': 5, 'STA': 6, 'SST': 7, 'SSS': 8,
                  'SSA': 9, 'SAT': 10, 'SAS': 11, 'SAA': 12, 'ATT': 4, 'ATS': 5, 'ATA': 6,
                  'AST': 7, 'ASS': 8, 'ASA': 9, 'AAT': 10, 'AAS': 11, 'AAA': 12, 'TT': 4,
                  'TS': 5, 'TA': 6, 'ST': 7, 'SS': 8, 'SA': 9, 'AT': 10, 'AS': 11, 'AA': 12,
                  'T': 1, 'S': 2, 'A': 3}

    for i in range(n-1, -1, -1):
        for j in range(13):
            for k in range(j, 13):
                tail1 = idx_list[j] + s[i]
                tail2 = idx_list[k] + s[i]
                dp_cur[j][k] = max(dp_pre[state_dict[tail1]][k] + attention_dict[tail1],
                                   dp_pre[j][state_dict[tail2]] + attention_dict[tail2])
                dp_cur[k][j] = dp_cur[j][k]
        dp_pre, dp_cur = dp_cur, dp_pre

    print(dp_pre[0][0])


n = int(input())
s = input()
colloquium(n, s)
