from typing import List
from functools import lru_cache
from functools import cache
# Write any import statements here


def create_pivots(N, R):
    piviots = [set() for i in range(N)]
    for i in range(N):
        piviots[i].add(R[i])

    for j in range(N)[::-1]:
        for i in range(j + 1)[::-1]:
            v = R[j] - (j - i)
            if v > i:
                piviots[i].add(v)

    return piviots



def getMinimumSecondsRequired(N: int, R: List[int], A: int, B: int) -> int:
    piviots = create_pivots(N, R)

    @lru_cache(maxsize=5000)
    def helper(pos, min_val):

        if pos == N:
            return 0
        piviots[pos].add(min_val)
        ans = float('inf')
        for cur_v in piviots[pos]:
            if cur_v < min_val:
                continue
            if R[pos] < cur_v:
                cur_cost = (cur_v - R[pos]) * A
            else:
                cur_cost = (R[pos] - cur_v) * B
            ans = min(ans, cur_cost + helper(pos + 1, cur_v + 1))
        return ans

    return helper(0, 1)


N = 6
R = [6, 5, 2, 4, 4, 7]
A = 1
B = 1
ans = getMinimumSecondsRequired(N, R, A, B)

print(ans)