import collections
import sys
import heapq
import math

def maximumLength(nums, k: int) -> int:
    n = len(nums)
    dp_heap = [list() for i in range(k + 2)]
    dp_dict = [dict() for i in range(k + 2)]

    dp_dict[0][nums[0]] = 1
    heapq.heappush(dp_heap[0], (-1, nums[0]))

    for i in range(1, n):
        for q in range(k + 1)[::-1]:
            if dp_heap[q]:
                length, tail = dp_heap[q][0]
            else:
                continue
            if tail == nums[i]:
                heapq.heappush(dp_heap[q], (length - 1, nums[i]))
                dp_dict[q][nums[i]] = -(length - 1)
            else:
                heapq.heappush(dp_heap[q + 1], (length - 1, nums[i]))
                dp_dict[q + 1][nums[i]] = max(dp_dict[q + 1].get(nums[i], 0), -(length - 1))
                if nums[i] in dp_dict[q]:
                    heapq.heappush(dp_heap[q], (-(dp_dict[q][nums[i]] + 1), nums[i]))
                    dp_dict[q][nums[i]] = max(dp_dict[q].get(nums[i], 0), (dp_dict[q][nums[i]] + 1))
        dp_dict[0][nums[i]] = max(dp_dict[0].get(nums[i], 0), 1)
        heapq.heappush(dp_heap[0], (-1, nums[i]))

    ans = 0
    for q in range(k + 1):
        if dp_heap[q]:
            ans = max(ans, -dp_heap[q][0][0])

    return ans


print(maximumLength([1, 1, 2], 0))


# print(maximumLength([1,2,3,4,5,1], 0))