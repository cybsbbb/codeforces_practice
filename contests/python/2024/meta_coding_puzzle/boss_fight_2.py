# meta_puzzles by Sebastien Rubens
#
# Please go to https://github.com/seb-pg/meta_puzzles/README.md
# for more information
#
# To the extent possible under law, the person who associated CC0 with
# meta_puzzles has waived all copyright and related or neighboring rights
# to meta_puzzles.
#
# You should have received a copy of the CC0 legalcode along with this
# work.  If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.

from typing import List
from dataclasses import dataclass, field


@dataclass
class DamageInfo:
    order: int = 0
    indices: List[int] = field(default_factory=lambda: [0, 0])
    damage: int = 0


def maximize_damage(N: int, H: List[int], D: List[int], info: DamageInfo):
    # this maximizes damage for a fixed index (max_i if order is True, otherwise max_j)
    # and also returns the value of max_i and max_j
    has_same_damage = True
    for i in range(N):
        index = info.indices[info.order]
        if index == i:
            continue
        if info.order == 0:
            new_damage = H[index] * D[index] + H[index] * D[i] + H[i] * D[i]
        else:
            new_damage = H[i] * D[i] + H[i] * D[index] + H[index] * D[index]
        if info.damage < new_damage:
            has_same_damage = False
            info.damage = new_damage
            info.indices[1 - info.order] = i
    return has_same_damage


def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
    # https://www.metacareers.com/profile/coding_puzzles/?puzzle=149169347195386
    # Constraints:
    #   2 ≤ N ≤ 500,000
    #   1 ≤ Hi ≤ 1,000,000,000
    #   1 ≤ Di ≤ 1,000,000,000
    #   1 ≤ B ≤ 1,000,000,000
    # Complexity: O(N^2)

    # we are maximizing H[i] * D[i] + H[i] * D[j] + H[j] * D[j] where i < j

    damage_infos = []  # This contains only two solutions and was done this way to make things look simpler
    for order in [0, 1]:
        damage_info = DamageInfo(order)
        while True:  # N iterations at most
            has_same_damage = maximize_damage(N, H, D, damage_info)  # N iterations
            if has_same_damage:
                break
            damage_info.order = 1 - damage_info.order
            damage_infos.append(DamageInfo(**damage_info.__dict__))
    if not damage_infos:
        return 0.
    damage_info = max(damage_infos, key=lambda d: d.damage)  # do not really need to set key
    return damage_info.damage / B


N = 3
H = [2, 1, 4]
D = [3, 1, 2]
B = 4
ans = getMaxDamageDealt(N, H, D, B)
print(ans)
