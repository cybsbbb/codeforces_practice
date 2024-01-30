from typing import List



def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:

    def calculate_demage(w1, w2):
        return w1[0] * w1[1] + w1[0] * w2[1] + w2[0] * w2[1]

    def calculate_max_damage(w1, w2):
        return max(calculate_demage(w1, w2), calculate_demage(w2, w1))

    warriors = sorted(list(zip(H, D)), key=lambda w: w[0] * w[1], reverse=True)
    top_warriors = [0, 1]
    cur_max = calculate_max_damage(warriors[top_warriors[0]], warriors[top_warriors[1]])

    while True:
        flag = False
        for i in range(N):
            if i in top_warriors:
                continue
            # replace 0
            tmp_top = [i, top_warriors[1]]
            tmp_demage = calculate_max_damage(warriors[tmp_top[0]], warriors[tmp_top[1]])
            if cur_max < tmp_demage:
                flag = True
                top_warriors = tmp_top
                cur_max = tmp_demage

            # replace 1
            tmp_top = [top_warriors[0], i]
            tmp_demage = calculate_max_damage(warriors[tmp_top[0]], warriors[tmp_top[1]])
            if cur_max < tmp_demage:
                flag = True
                top_warriors = tmp_top
                cur_max = tmp_demage

        if not flag:
            break

    return cur_max / B

N = 3
H = [2, 1, 4]
D = [3, 1, 2]
B = 4
ans = getMaxDamageDealt(N, H, D, B)
print(ans)
