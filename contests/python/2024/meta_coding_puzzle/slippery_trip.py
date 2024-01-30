from typing import List


# Write any import statements here


def getMaxCollectableCoins(R: int, C: int, G: List[List[str]]) -> int:
    # Write your code here

    def get_row_info(row):
        is_down = False
        is_right = False
        right_cnt = 0

        last_right = -1
        tot_star = 0
        cur_star = 0
        max_interval = 0

        for i in range(C):
            if row[i] == '>':
                is_right = True
                right_cnt += 1
                if last_right == -1:
                    last_right = i
            elif row[i] == 'v':
                is_down = True
                if last_right != -1:
                    max_interval = max(max_interval, cur_star)
                    last_right = -1
                    cur_star = 0
            elif row[i] == '*':
                tot_star += 1
                if last_right != -1:
                    cur_star += 1

        if last_right >= 0 and is_down:
            for i in range(C):
                if row[i] == '*':
                    cur_star += 1
                elif row[i] == 'v':
                    max_interval = max(max_interval, cur_star)
                    break

        return (right_cnt < C), max(max_interval, int(tot_star > 0)), (not is_down and is_right), tot_star

    ans = 0
    cur_val = 0
    for row in G:
        can_down, down_max, can_trap, trap_max = get_row_info(row)
        print(can_down, down_max, can_trap, trap_max)
        if can_trap:
            ans = max(ans, cur_val + trap_max)
        if can_down:
            cur_val += down_max
        else:
            break
    ans = max(ans, cur_val)
    return ans


